import socket
import threading
import rsa
import hashlib
from db import create_table, verify_user

# Generate RSA keys
public_key, private_key = rsa.newkeys(1024)
public_partner = None

def handle_client(client_socket):
    global public_partner
    client_socket.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

    # Verify user
    client_socket.send(b"Enter username: ")
    username = client_socket.recv(1024).decode()
    client_socket.send(b"Enter password: ")
    password = client_socket.recv(1024).decode()

    if verify_user(username, password):
        client_socket.send(b"Login successful. Ready to chat with host.")
        print(f"{username} joined the chat.")
    else:
        client_socket.send(b"Login failed. Disconnecting.")
        client_socket.close()
        return

    def send_messages():
        while True:
            message = input("")
            digest = hashlib.sha256(message.encode()).digest()
            signature = rsa.sign(digest, private_key, 'SHA-256')
            try:
                client_socket.sendall(rsa.encrypt(message.encode(), public_partner) + b"::" + signature)
                print("You: " + message)
            except Exception as e:
                print(f"Failed to send message: {e}")
                break

    def receive_messages():
        while True:
            try:
                data = client_socket.recv(4096)  # Increased buffer size for longer messages
                if data:
                    encrypted_message, signature = data.split(b"::")
                    message = rsa.decrypt(encrypted_message, private_key).decode()
                    digest = hashlib.sha256(message.encode()).digest()
                    try:
                        rsa.verify(digest, signature, public_partner)
                        print(username +": " + message + "       - VERIFIED -")
                    except rsa.VerificationError:
                        print(username +": " + " (Message verification failed)")
                else:
                    print("Connection closed by the client.")
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    threading.Thread(target=send_messages).start()
    threading.Thread(target=receive_messages).start()

def main():
    create_table()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  # Bind to all interfaces
    server.listen(1)
    print("Waiting for a connection...")
    client_socket, addr = server.accept()
    print(f"Connection established with {addr}.")

    handle_client(client_socket)

if __name__ == "__main__":
    main()
