from flask import render_template, url_for, flash, redirect,request,make_response
from pro import app,db 
from pro.form import *
from pro.model  import User
from flask_login import login_user,current_user,logout_user,login_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
)
@app.route("/dash",methods = ["GET","POST"])
@login_required
def dash():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    name = None
    form = MainForm()
    res = make_response(render_template("dashborad.html",form=form))   

    if request.method == "POST":
        name = request.form.get("username")
        res.set_cookie("name",name,max_age=24*60*60*1000) # 1 day 
        print("DONE")
    return res



@app.route("/", methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dash'))
    form = LoginForm()
    if form.validate_on_submit():
        user_check = User.query.filter_by(username=form.username.data).first()
        try:
            if user_check.password == form.password.data:
 
                login_user(user_check,remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('dash'))# %2 
            else:
                flash('Login Unsuccessful. username = admin | password = 123123', 'danger')
        except:
            flash('Login Unsuccessful. username = admin | password = 123123', 'danger')

    return render_template('index.html', title='Login', form=form)



@app.route("/logout")
@login_required# we need to login
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    logout_user()
    return redirect(url_for('login'))