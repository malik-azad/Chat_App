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
   git clone https://github.com/malik-azad/Chat_App.git
   cd Chat_App
2. **Install dependencies:**
   ```sh
   pip install rsa
  
# Usage
## Step 1: Set up the Database
### Run db.py to create the database and user table:
    python db.py
    
## Step 2: Manage Users
### Add users using the functions provided in db.py
      from db import add_user, update_user, view_users, delete_user
   
      # Add a user
      add_user('username', 'password')
      
      # Update a user's password
      update_user('username', 'new_password')
      
      # View all users
      print(view_users())
      
      # Delete a user
      delete_user('username')

 ## Step 3: Start the Server
 ### Run the server script:
       python server.py

 The server will start listening for incoming connections on port 9999.
   
## Step 4: Connect with the Client
### Run the client script:
      python client.py
      
 The client will automatically connect to the server using the IP address defined in the script. You will be prompted to enter your username and password.

## Successful Login
 The server displays: username joined the chat. <br>
 The client displays: Successful login, ready to chat with host.<br>

## Chatting
 After logging in, you can start sending and receiving encrypted messages. <br>
 The messages are signed and verified using RSA digital signatures to ensure integrity and authenticity.

## Project Structure
 db.py: Handles user registration, login, and database operations. <br>
 server.py: Manages incoming connections and facilitates secure communication. <br>
 client.py: Connects to the server and handles sending and receiving messages.

## Fell free to update/modify this project

 Made with 🤍 by [Malik Azad](https://www.linkedin.com/in/malikazad)

 
  [![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/malikazad) 


