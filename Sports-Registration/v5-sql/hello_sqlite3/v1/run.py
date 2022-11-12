import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()

query = "DROP TABLE IF EXISTS REGISTRANTS;"
cur.execute(query)
query = "CREATE TABLE REGISTRANTS (name TEXT NOT NULL, sport TEXT NOT NULL);"
cur.execute(query)

query = "INSERT INTO REGISTRANTS VALUES ('{}', '{}')".format
cur.execute(query("Alice", "Basketball"))
cur.execute(query("Bob", "Soccer"))
cur.execute(query("Carol", "Ultimate Frisbee"))

rows = cur.execute("SELECT * FROM REGISTRANTS").fetchall()
print(rows)
print("__DONE__")
