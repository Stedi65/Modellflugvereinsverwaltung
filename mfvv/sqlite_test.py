import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("CREATE TABLE users (name TEXT, addr TEXT)")
name = "Stephan"
addr = "Rahden"
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, addr) VALUES (?,?)", (name, addr))
conn.commit()
conn.close()