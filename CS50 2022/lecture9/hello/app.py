from flask import Flask, render_template, request


app = Flask(__name__)

# Whenever the user finds himself on the page "/"...
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # ... spit out all of index.html's contents
        return render_template('index.html')
    elif request.method == 'POST':
        # request.args for GET | request.form for POST
        return render_template('greet.html', name=request.form.get('name', 'world'))
