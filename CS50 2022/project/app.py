from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from functions import login_required, usd, decimal

from datetime import date


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tmanager.db")


@app.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()
    msg = ['Welcome back!', 'To continue, please log in']

    if request.method == 'POST':
        user = request.form.get('username')
        pssw = request.form.get('password')
        if not user or not pssw:
            msg = ['Invalid login', 'Please make sure username and password blanks are filled in']
            return render_template('login.html', msg=msg)

        find_user = db.execute('SELECT * FROM users WHERE username = ?', user)
        if not find_user or not check_password_hash(find_user[0]['hash'], pssw):
            msg = ['Invalid username and/or password', 'Be sure to type username and password correctly and check if caps lock is not on']
            return render_template('login.html', msg=msg)

        session['user_id'] = find_user[0]['id']

        return redirect('/')

    else:
        return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ['Welcome!', 'To start your experience, please register in']

    if request.method == 'POST':

        user = request.form.get('username')
        pssw = request.form.get('password')
        confirm = request.form.get('confirm')
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))

        if not user or not pssw or not confirm or not year or not month or not day:
            msg = ['Invalid registration', 'Please make sure username and password blanks are filled in']
            return render_template('register.html', msg=msg)
        elif len(user) < 4:
            msg = ['Invalid username', 'Username must contain at least 4 characters']
            return render_template('register.html', msg=msg)
        elif len(pssw) < 8:
            msg = ['Invalid password', 'Password must contain at least 8 characters']
            return render_template('register.html', msg=msg)
        elif pssw != confirm:
            msg = ['Passwords do not match', 'Be sure both password and its confirmation match']
            return render_template('register.html', msg=msg)

        if age(year, month, day) < 18:
            msg = ['Underage restriction', 'User must be at least 18 years old to register']
            return render_template('register.html', msg=msg)

        find_user = db.execute('SELECT * FROM users WHERE username = ?', user)
        if find_user:
            msg = ['Invalid username', 'Username already exists']
            return render_template('register.html', msg=msg)

        hash = generate_password_hash(pssw)
        db.execute('INSERT INTO users (username, hash, year, month, day) VALUES (?, ?, ?, ?, ?)', user, hash, year, month, day)

        return redirect('/login')

    else:
        return render_template('register.html', msg=msg)


def age(year, month, day):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age


@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


@app.route('/')
@login_required
def index():
    user_id = session['user_id']
    user = db.execute('SELECT * FROM users WHERE id = ?', user_id)
    income = user[0]['income']
    tasks = len(db.execute('SELECT * FROM user_todo WHERE user_id = ?', user_id))

    if user[0]['height'] and user[0]['weight']:
        bmi = decimal(float(user[0]['weight'])/(float(user[0]['height'])**2))
    else:
        bmi = None

    return render_template('index.html', income=income, tasks=tasks, bmi=bmi, usd=usd)


@app.route('/balance', methods=['GET', 'POST'])
@login_required
def balance():
    user_id = session['user_id']

    msg = ['Balance', 'Here you can manage your financial balance along with all of your added operations']

    if request.method == 'POST':
        add = request.form.get('add')
        desc = request.form.get('desc')
        type = request.form.get('type')
        amnt = request.form.get('amnt')

        clear = request.form.get('clear')

        income = request.form.get('income')

        if add:
            amnt = int(amnt)
            if not desc or not type or not amnt:
                msg = ['Incomplete feedback', 'Be sure to fill out all blanks']
                return render_template('balance.html', msg=msg, usd=usd)
            elif amnt <= 0:
                msg = ['Invalid amount', 'Please type a valid amount']
                return render_template('balance.html', msg=msg, usd=usd)

            if type == 'Retract':
                amnt = amnt * (-1)

            db.execute('INSERT INTO cash_flow (user_id, name, amount) VALUES (?, ?, ?)', user_id, desc, amnt)
            cur_balance = int(db.execute('SELECT income FROM users WHERE id = ?', user_id)[0]['income'])
            db.execute('UPDATE users SET income = ? WHERE id = ?', cur_balance+amnt, user_id)
        elif clear:
            db.execute('DELETE FROM cash_flow WHERE user_id = ?', user_id)
        else:
            income = int(income)
            if income <= 0:
                msg = ['Invalid amount', 'Please type a valid amount']
                return render_template('balance.html', msg=msg, usd=usd)

            cur_balance = db.execute('SELECT income FROM users WHERE id = ?', user_id)[0]['income']
            if cur_balance:
                db.execute('UPDATE users SET income = ? WHERE id = ?', cur_balance+income, user_id)
            else:
                db.execute('UPDATE users SET income = ? WHERE id = ?', income, user_id)

        return redirect('/balance')

    else:
        cur_balance = db.execute('SELECT income FROM users WHERE id = ?', user_id)[0]['income']
        cash_flow = db.execute('SELECT * FROM cash_flow WHERE user_id = ?', user_id)

        if cur_balance != None and cash_flow:
            return render_template('balance.html', balance=cur_balance, operations=cash_flow, usd=usd, msg=msg)
        elif cur_balance != None and not cash_flow:
            return render_template('balance.html', balance=cur_balance, no_ops=1, usd=usd, msg=msg)

        msg = ['Lack of info', 'Your current income and operations are not yet set']
        return render_template('balance.html', no_income=1, no_ops=1, msg=msg, usd=usd)


@app.route('/todo', methods=['GET', 'POST'])
@login_required
def todo():
    msg = ['Welcome to your to do list', 'Here you\'ll be able to add or remove your tasks']

    if request.method == 'POST':
        add = request.form.get('add')
        title = request.form.get('title')
        desc = request.form.get('desc')
        time = request.form.get('time')

        remove = request.form.get('remove')
        task = request.form.get('task')

        clear = request.form.get('clear')

        user_id = session['user_id']

        if clear:
            db.execute('DELETE FROM user_todo WHERE user_id = ?', user_id)
            return redirect('/todo')

        if remove and not task:
            msg = ['Incomplete feedback', 'Please make sure to fill out all blanks2']
            return render_template('todo.html', msg=msg)
        elif remove and task:
            db.execute('DELETE FROM user_todo WHERE user_id = ? AND title = ?', user_id, task)
            return redirect('/todo')

        if add and not title or not desc or not time:
            msg = ['Incomplete feedback', 'Please make sure to fill out all blanks1']
            return render_template('todo.html', msg=msg)
        else:
            db.execute('INSERT INTO user_todo (user_id, title, description, time) VALUES (?, ?, ?, ?)', user_id, title, desc, time)

        return redirect('/todo')

    else:
        user_id = session['user_id']
        tasks = db.execute('SELECT * FROM user_todo WHERE user_id = ?', user_id)

        return render_template('todo.html', tasks=tasks, msg=msg)


@app.route('/password', methods=['GET', 'POST'])
@login_required
def password():
    msg = ['Password change', 'Here you can change your password, keep in mind it must contain at least eight characters']

    if request.method == 'POST':
        old_p = request.form.get('old')
        new_p = request.form.get('new')
        confirm = request.form.get('confirm')

        if not old_p or not new_p or not confirm:
            msg = ['Invalid feedback', 'Please make sure to fill out all blanks']
            return render_template('password.html', msg=msg)
        elif new_p != confirm:
            msg = ['Passwords do not match', 'Make sure to type passwords correctly and check if your caps lock is off']
            return render_template('password.html', msg=msg)
        elif len(new_p) < 8:
            msg = ['Invalid password', 'Make sure to create a password at least 8 characters long']
            return render_template('password.html', msg=msg)

        user_id = session['user_id']
        cur_p = db.execute('SELECT * FROM users WHERE id = ?', user_id)[0]['hash']
        if not check_password_hash(cur_p, old_p):
            msg = ['Incorrect password', 'Make sure to type your current password correctly and check if your caps lock is off']
            return render_template('password.html', msg=msg)

        hash = generate_password_hash(new_p)
        db.execute('UPDATE users SET hash = ? WHERE id = ?', hash, user_id)

        return redirect('/logout')

    else:
        return render_template('password.html', msg=msg)


@app.route('/fitness', methods=['GET', 'POST'])
@login_required
def fitness():
    msg = ['Welcome to your fitness advisor', 'Here you will be able to inform yourself into a healthier lifestyle']

    if request.method == 'POST':
        system = request.form.get('system')
        weight = request.form.get('weight')
        height = request.form.get('height')

        if not weight or not height or not system:
            msg = ['Invalid feedback', 'Please make sure to fill out all blanks']
            return render_template('fitness.html', msg=msg)

        if system == 'Metric':
            if '.' not in height and ',' not in height and len(height) == 4:
                height = float(height)/100
            elif ',' in height:
                height = float(height.replace(',', '.'))
            else:
                height = float(height)

            if ',' in weight:
                weight = float(weight.replace(',', '.'))
            else:
                weight = float(weight)
        elif system == 'Imperial':
            height = float(height)*30.48/100
            weight = float(weight)/2.2
        else:
            msg = ['Invalid feedback', 'Please make sure to complete blanks correctly']
            return render_template('fitness.html', msg=msg)

        if weight <= 0 or height <= 0:
            msg = ['Invalid feedback', 'Please make sure to give valid answers']
            return render_template('fitness.html', msg=msg)

        user_id = session['user_id']
        db.execute('UPDATE users SET height = ?, weight = ? WHERE id = ?', height, weight, user_id)

        return redirect('/fitness')

    else:
        user_id = session['user_id']
        user = db.execute('SELECT * FROM users WHERE id = ?', user_id)
        weight = user[0]['weight']
        height = user[0]['height']

        if not weight and not height:
            return render_template('fitness.html', no_data=1, msg=msg)

        weight = float(weight)
        height = float(height)

        bmi = decimal(weight/(height**2))
        if bmi < 18:
            message = f'BMI: { bmi }, underweight: You present to be underweight according to your submitted info.'
        elif bmi > 25:
            message = f'BMI: { bmi }, overweight: You present to be overweight according to your submitted info.'
        elif bmi > 30:
            message = f'BMI: { bmi }, obesety: You present to be obese according to your submitted info.'
        else:
            message = f'BMI: { bmi }, healthy: You present to have a healthy weight according to your submitted info.'

        ad_weight = decimal(21.5*(height**2))
        water = decimal(weight*0.035)

        disclaimer = 'Remember this is just an estimate, do not take this as an accurate diagnosis. For more info, please consult your trusted doctor.'

        return render_template('fitness.html', bmi=bmi, message=message, weight=ad_weight, water=water, disclaimer=disclaimer, decimal=decimal, msg=msg)


def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    print(e.name, e.code)
    return

for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
