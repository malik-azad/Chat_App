import sqlite3

def create_table():
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    conn.close()

def update_user(username, new_password):
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
    conn.commit()
    conn.close()
    print("User updated successfully.")

def view_users():
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    for user in users:
        print(user)

def delete_user(username):
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()
    print("User deleted successfully.")


def verify_user(username, password):
    conn = sqlite3.connect('chatapp.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

if __name__ == "__main__":
    create_table()
    add_user('jubran', 123)
    view_users()

    res = verify_user('azad', 123)
    print(res)



