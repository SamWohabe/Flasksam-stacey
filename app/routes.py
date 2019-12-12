from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/personality', methods=['GET', 'POST'])
def personfont():
    user_input=dict(request.form)
    print(user_input)
    x=user_input["personality"]
    print(x)
    output=model.personfont(x)
    print(output)
    return render_template('index2.html', output=output)
