import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, usersurname, useremail) VALUES (?, ?, ?)", ('Username1', 'Usersurname1', 'User1@email.com'))
cur.execute("INSERT INTO users (username, usersurname, useremail) VALUES (?, ?, ?)", ('Username2', 'Usersurname2', 'User2@email.com'))

connection.commit()
connection.close()