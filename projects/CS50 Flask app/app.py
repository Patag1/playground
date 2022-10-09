# from flask import Flask, redirect, render-template, request
# from cs50 import SQL

from crypt import methods
from urllib import request


app = Flask(__name__)

db = SQL('sqlite:///froshims.db')

SPORTS = [
    'Basketball',
    'Soccer',
    'Football'
]

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)

@app.route('/deregister', methods=['POST'])
def deregister():

    # Forget registrant
    id = request.args.get('id')
    if id:
        db.execute('DELETE FROM registrants WHERE id = ?', id)
    return redirect('/registrants')

@app.route('/register', methods=["POST"])
def register():

    # Validate submission
    name = request.args.get('name')
    sport = request.args.get('sport')
    if not name or sport not in SPORTS:
        return render_template('failure.html')
    
    # Remember registrant
    db.execute('INSERT INTO registrants (name, sport) VALUES(?, ?)', name, sport)

    # Confirm registration
    return redirect('/registrants')

@app.route('/registrants')
def registrants():
    registrants = db.execute('SELECT * FROM registrants')
    return render_template('registrants.html', registrants=registrants)