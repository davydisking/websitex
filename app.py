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
  



class join(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    Joins = db.relationship('Frequency', backref='joins') 




    
    def __repr__(self):
        return '<Name%r>' % self.id
        

@app.route('/', methods=['POST', 'GET'])
def index():
    #users = Frequency.query.all()
    return render_template("index.html")

@app.route('/get_input', methods=['POST'])
def get_input():        
    sign_in = request.form['name'] 
    
    in_sign = Frequency(name=sign_in, password=request.form['password'], email=request.form['Email']  )
        
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

@app.route('/family', methods=['POST'])
def family():
    name=request.form['name']
    password=request.form['password']
    email=request.form['email'] 
    phone=request.form['phone'] 
    company=request.form['company']
    address=request.form['address']      
     
    
    joining = join(name=name, password=password, email=email, phone=phone, company=company, address=address  )
        
    try:        
        db.session.add(joining)        
        db.session.commit()       
        return redirect('/upload/')
    except:
        return "An error occurred"


if __name__ == "__main__":
    app.run(debug=True)
