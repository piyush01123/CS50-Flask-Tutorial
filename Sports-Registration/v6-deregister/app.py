from  flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

def get_db_connection():
	conn = sqlite3.connect("database.db")
	conn.row_factory = sqlite3.Row
	return conn

@app.route('/')
def index():
	return render_template("index.html", sports=SPORTS)

@app.route('/register', methods=["POST"])
def register():
	name= request.form.get("name")
	sport = request.form.get("sport")
	if not name or sport not in SPORTS:
		return render_template("failure.html")
	conn = get_db_connection()
	conn.execute("INSERT INTO REGISTRANTS (name, sport) VALUES(?, ?)", (name, sport))
	conn.commit()
	conn.close()
	return redirect("/registrants")

@app.route('/deregister', methods=["POST"])
def deregister():
	id = request.form.get("id")
	conn = get_db_connection()
	conn.execute("DELETE FROM REGISTRANTS WHERE id==?", id)
	conn.commit()
	conn.close()
	return redirect("/registrants")

@app.route('/registrants')
def registrants():
	conn = get_db_connection()
	REGISTRANTS = conn.execute("SELECT * FROM REGISTRANTS").fetchall()
	conn.close()
	return render_template("registrants.html", registrants=REGISTRANTS)

app.run("0.0.0.0",5000)
