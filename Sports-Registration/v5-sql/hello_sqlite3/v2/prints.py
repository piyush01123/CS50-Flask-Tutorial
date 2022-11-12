import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
rows = cur.execute("SELECT * FROM REGISTRANTS").fetchall()
print(rows)
