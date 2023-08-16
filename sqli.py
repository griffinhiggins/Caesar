import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
cursor.execute("INSERT INTO users (username, password) VALUES ('Griffin', 'passwd')")
cursor.execute("INSERT INTO users (username, password) VALUES ('Shabnam', 'password123')")

username = input("Enter username: ")
password = input("Enter password: ")

query = f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'"
cursor.execute(query)

result = cursor.fetchall()
for row in result:
    print(row)

conn.close()
