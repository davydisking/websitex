from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import sqlite

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'SQLITE:///login.db'
db = SQLAlchemy(app)

class Friends(db.model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(200), nullable=False)
    email = db.column(db.string(200), nullable=False)
    date_created = db.column(db.Datetime, default=datetime.utcnow)       

    def __repr__(self):
        return '<name %r>' % self.id

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods = ["POST"])
def index():
    UN = request.form['name']
    PW = request.form['password']

    sqlconnection = sqlite3.connection(currentlocation + "\login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password from users WHERE Username = '{un}' AND Password = '{pw})'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("index.html")
    else:
        return redirect("/Getstarted")
    
@app.route("/Getstarted", methods= ["POST", "GET"])
def Getstarted():
    if request.method == "POST":
        dUN = request.form['Username']
        dPW = request.form['Password']
        Uemail = request.form['emailuser']
        sqlconnection = sqlite3.connection(currentlocation + "\login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO users VALUES('{u}','{p}','{e}')".format (u = dUN, p = dPW, e = Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("index.html")





@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")


@app.route('/upload/')
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)