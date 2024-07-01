import socket
import threading
import rsa
import hashlib

# Generate RSA keys
public_key, private_key = rsa.newkeys(1024)
public_partner = None

def send_messages(client_socket):
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

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(4096)  # Increased buffer size for longer messages
            if data:
                encrypted_message, signature = data.split(b"::")
                message = rsa.decrypt(encrypted_message, private_key).decode()
                digest = hashlib.sha256(message.encode()).digest()
                try:
                    rsa.verify(digest, signature, public_partner)
                    print("Host: " + message  + "      -VERIFIED-" )
                except rsa.VerificationError:
                    print("Partner: (Message verification failed)")
            else:
                print("Connection closed by the server.")
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP address: ") # IP address of server(azad)
    try:
        client_socket.connect((server_ip, 9999))
        global public_partner
        public_partner = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))
        client_socket.send(public_key.save_pkcs1("PEM"))
        print("Connected to the server.")

        # Login
        print(client_socket.recv(1024).decode()) 
        username = input()
        client_socket.send(username.encode())
        print(client_socket.recv(1024).decode())
        password = input()
        client_socket.send(password.encode())
        login_response = client_socket.recv(1024).decode()
        print(login_response)
        if "Login failed" in login_response:
            client_socket.close()
            return

    except Exception as e:
        print(f"Failed to connect to the server: {e}")
        return

    threading.Thread(target=send_messages, args=(client_socket,)).start()
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
