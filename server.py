from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from wtforms import Form, StringField, validators

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The_secret_key'

@app.route("/users", methods=('GET', 'POST'))
def users():
    if request.method == 'GET':
     conn = get_db_connection()
     users = conn.execute('SELECT * FROM users').fetchall()
     conn.close()
     return render_template('users.html', users=users)

class ValidateForm(Form):
    username = StringField('username', [validators.Length(min=1, max=25)])
    usersurname = StringField('usersurname', [validators.Length(min=1, max=25)])
    useremail = StringField('useremail', [validators.Length(min=6, max=35)])

@app.route('/', methods=('GET', 'POST'))
def index():
    form = ValidateForm(request.form)
    if request.method == 'POST' and form.validate():

        username = request.form['username']
        usersurname = request.form['usersurname']
        useremail = request.form['useremail']

        conn = get_db_connection()
        user = conn.execute("SELECT rowid FROM users WHERE (username = ? AND usersurname = ?)", (username, usersurname)).fetchall()
        
        if len(user) == 0:

            conn.execute("INSERT INTO users (username, usersurname, useremail) VALUES (?, ?, ?)", (username, usersurname, useremail))
            conn.commit()
            conn.close()

            return render_template('hello.html', message="Hello, ", name=username, surname=usersurname)
        else:
            conn.close()
            return render_template('hello.html', message="Already seen you, ", name=username, surname=usersurname)

    return render_template('index.html')

@app.route('/hello', methods=('GET', 'POST'))
def hello():
    return render_template('hello.html')
