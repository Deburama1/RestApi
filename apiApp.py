from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, render_template, url_for,flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/dataQuery'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), unique=True)
    contents = db.Column(db.String(255), unique=True)
    views = db.Column(db.Integer, primary_key=True)   
    timestamp = db.Column(db.DateTime())

@app.route('/')
def index():
    # list of object
    return render_template('index.html') #should be web application given by user

def EQUAL(property,value):
   return User.query.filter_by(property=value).all()

def AND(a,b):
   return User.query.filter_by(a).filter_by(b).all()

def OR(a,b):
    list = User()
    list = User.query.filter_by(a).all() or User.filter_by(b).all()
    return list




@app.route('/post_user', methods=['GET','POST'])
def post_user():
    if request.method == 'POST':
        if not request.form['id'] or not request.form['title'] or not request.form['content'] or not request.form['views'] or not request.form['timestamp']:       
            flash('Please enter all the fields', 'error')
        else:
            user = User(request.form['id'],request.form['title'],request.form['content'],request.form['views'], request.form['timestamp'])
    elif request.method == 'GET':
        args = request.args
        id = args.get('id')
        title = args.get('title')
        contents = args.get('contents')
        views = args.get('views')
        timestamp = args.get('timestamp')
        



    # this add to the database the user
    db.session.add(user)
    # this saves this data in the database
    db.session.commit()
    return redirect(url_for('index'))