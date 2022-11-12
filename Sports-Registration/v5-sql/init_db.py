import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
query = "DROP TABLE IF EXISTS REGISTRANTS;"
cur.execute(query)
query = "CREATE TABLE REGISTRANTS (name TEXT NOT NULL, sport TEXT NOT NULL);"
cur.execute(query)
conn.commit()
conn.close()
