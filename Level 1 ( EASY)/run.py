from flask import Flask,render_template,make_response,request,url_for
from form import * 
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/dash")
def dash():
    return render_template("dashborad.html") 

@app.route("/",methods = ["GET","POST"])
def index():
    form = MainForm()
    if request.method == "POST":
  
        if len(request.form.get("csrf_token")) <=30:
            error = "Valid Token !!"
            return "INVALID TOKEN !!" 
        username = request.form.get("username")
        password = request.form.get("password")
            
        if username == "admin" and password == "123123":

            res = make_response("")
            res.headers["location"] = url_for('dash') # عشان يتم توجيه ل صفحه ثانيه ولازم نحط ستاوس كود 302 فورديبل
            return res,302
        else:
            error = "Username or password is invalid"
            return render_template("index.html",error=error,form=form)


    return render_template("index.html",form=form)

@app.route("/cookie")
def cookie():
    if not (request.cookies.get("cookies")):
        res = make_response("setting a cookie")
        res.set_cookie("cookies",secrets.token_hex(16),max_age=24*60*60*1000) # 1 day 
    else:
        res = make_response(f"Value of cookie foo is <h1>{request.cookies.get('foo')}")
    return res 

@app.route("/delete")
def delete():
    res = make_response("cookie Removed")
    res.set_cookie("cookies","DELETE",max_age=0)
    return res

app.debug = True
app.run()