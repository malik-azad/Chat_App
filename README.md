# Secure Chat App

This project implements a secure chat application using RSA encryption for digital signatures and message encryption. The app uses a client-server architecture where users need to register and log in before they can send and receive messages. The server verifies user credentials, manages connections, and facilitates secure communication between users.

## Features

- **User Registration and Login:** Users must register with a username and password before logging in.
- **RSA Encryption:** Messages are encrypted using RSA public-private key pairs.
- **Digital Signatures:** Messages are signed with the sender's private key and verified with the sender's public key.
- **SQLite Database:** User credentials are stored securely in an SQLite database.
- **Client-Server Architecture:** The server manages connections and ensures secure communication between clients.

## Requirements

- Python 3.6 or higher
- `rsa` library
- `sqlite3` library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/secure-chat-app.git
   cd secure-chat-app


Install dependencies:
sh
Copy code
pip install rsa
Usage
Step 1: Set up the Database
Run db.py to create the database and user table:
