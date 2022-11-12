import sqlite3
conn = sqlite3.connect("store.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS BOOKS;")
cur.execute("CREATE TABLE BOOKS (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))")
for title in open("harry_potter_series.txt",'r').readlines():
	cur.execute("INSERT INTO BOOKS (title) VALUES (?)", (title.strip(),))
titles = cur.execute("SELECT * FROM BOOKS").fetchall()
print(titles)
conn.commit()
conn.close()
