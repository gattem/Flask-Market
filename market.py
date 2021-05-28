from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////mnt/c/users/anto/doctumets/database_files/filestorage.db'
db = SQLAlchemy(app)

# class FileContents(db.model):
#     id=db.coloum(db.Integer,Primary_key=True)
#     name = db.coloum(db.String(300))
#     data= db.coloum(db.LargeBinary)



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/upload' , methods = ['POST','GET'])
def upload():
    file = request.files['fileToUpload']
    return file.filename


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'plan': 'silver', 'storage': '10', 'price': 10},
        {'id': 2, 'plan': 'Gold', 'storage': '100', 'price': 90},
        {'id': 3, 'plan': 'Diamond', 'storage': '1000', 'price': 500}
    ]
    return render_template('market.html', items=items)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/forget')
def forgot_page():
    return render_template('forgot.html')
@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=True)

