import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
query = "DROP TABLE IF EXISTS REGISTRANTS;"
cur.execute(query)
query = "CREATE TABLE REGISTRANTS (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));"
cur.execute(query)
conn.commit()
conn.close()
