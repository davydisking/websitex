from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate, migrate



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Frequency.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sapele10035@localhost/Frequency_1'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Frequency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.Integer, nullable=False)     
    
    def __repr__(self):
        return f'Name: {self.name}'

@app.route('/', methods=['POST', 'GET'])
def index():
    users = Frequency.query.all()
    return render_template("index.html", users=users)

@app.route('/get_input', methods=['POST'])
def get_input(): 
    print('hello')
    print(request.form)        
    name = request.form['name']
    email=request.form['Email']
    password = request.form['password']
    
    in_sign = Frequency(name=name, email=email, password=password)
    
    try:
        db.session.add(in_sign)
        db.session.commit()
        return redirect('/')
    except:
        return "An error occurred"


@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")


@app.route('/upload/')
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
