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
    #Joins = db.relationship('join', backref='joins') 



class join(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    password = db.Column(db.Integer, nullable=False)
    #join_frequency_FK = db.Column(db.Integer, db.ForeignKey('frequency.id'))

class upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

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

@app.route('/family/', methods=['POST'])
def family():
    name=request.form['name'] 
    phone=request.form['phone'] 
    email=request.form['email']
    company=request.form['company']
    password=request.form['password']      
     
    
    joining = join(name=name, password=password, email=email, phone=phone, company=company)
        
    try:        
        db.session.add(joining)       
        db.session.commit()      
        return redirect('/upload')
    except:
        return "An error occurred"

@app.route('/post_job', methods=['POST'])
def post_job():
    img = request.files['image']
    position=request.form['position']
    payment=request.form['payment']
    location=request.form['location']

    posting = upload(img=image.read(), position=position, payment=payment, location=location)

    try:        
        db.session.add(posting)       
        db.session.commit()      
        return redirect('/upload')
    except:
        return "An error occurred"



if __name__ == "__main__":
    app.run(debug=True)
