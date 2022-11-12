from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_db_connection():
	conn = sqlite3.connect("store.db")
	conn.row_factory = sqlite3.Row
	return conn

@app.route('/')
def index():
	conn = get_db_connection()
	titles = conn.execute("SELECT * FROM BOOKS").fetchall()
	return render_template("index.html", titles=titles)

@app.route('/cart', methods=["GET","POST"])
def cart():
	if "cart_items" not in session:
		session["cart_items"] = []
	if request.method=="POST":
		session["cart_items"].append(request.form.get("id"))
		return redirect('/cart')
	conn = get_db_connection()
	query = "SELECT * FROM BOOKS WHERE id IN ({})".format(','.join(session["cart_items"]))
	print(query)
	titles = conn.execute(query).fetchall()
	return render_template("/cart.html", titles=titles)

app.run("0.0.0.0",5000)
