import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()
query = "INSERT INTO REGISTRANTS (name, sport) VALUES (?, ?)"
cur.execute(query, ("Alice", "Basketball"))
cur.execute(query, ("Bob", "Soccer"))
cur.execute(query, ("Carol", "Ultimate Frisbee"))
conn.commit()
conn.close()
