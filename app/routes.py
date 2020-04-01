from app import app
from flask import render_template, flash, redirect, make_response, request
from app.forms import LoginForm

@app.route('/', methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "michael" and form.password.data == "test12345":
            resp = make_response(redirect('/account'))
            resp.set_cookie('username', "michael")
            return(resp)
        else:
            flash('Invalid Credentials')
    return render_template("vuln_cookie.html", form=form)

@app.route('/account', methods=['GET'])
def account():
    username = request.cookies.get('username')
    if username == "michael":
        balance = "$21.53"
    if username == "elon":
        balance = "$3,984,195,3432"
    return f"Welcome {username}! Your balance is {balance}"
