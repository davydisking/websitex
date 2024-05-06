from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Frequency.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sapele10035@localhost/Frequency_test'
db = SQLAlchemy(app)

class Frequency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.Integer, nullable=False)     
    
    def __repr__(self):
        return '<Name %r>'%self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == "POST"):
        sign_in = request.form['name']
        in_sign = Frequency(name=sign_in ,password=request.form['password'], email=request.form['Email'])

        try:
            db.session.add(in_sign)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "An error occurred"
    
    else:
        return render_template('index.html')


@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")


@app.route('/upload/')
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)