import os

from flask import Flask, render_template, request
from sqlalchemy.sql import text
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha1_crypt

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)

sql = "select * from passwords WHERE substring(hash for 7) = substring(digest('{password_string}','sha1') for 7) and hash = digest('{password_string}','sha1')"

@app.route('/')
def view_registration_form():
    return render_template('pw_form.html')



@app.route('/register', methods=['POST'])
def register_guest():
    password_string = request.form.get('password_string')
    results = db.engine.execute(text(sql.format(password_string=password_string)))
    for pw_number in results:
        return render_template(
            'pw_result.html', myresult="You have found the pwned password number {pw_number}!".format(pw_number=pw_number['id']))
    return render_template(
        'pw_result.html', myresult="Sorry, it's a fail!")
