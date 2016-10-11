from flask import Flask, render_template, request, session, redirect, url_for
from utils import login
import os
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/login")
def getForm():
    if "Username" in session:
        redirect(url_for('mainPage'))
    return render_template('form.html')

@app.route("/authenticate/", methods = ['POST'])
def auth():
    text = "ERROR"
    password = hashlib.sha256(request.form["Password"]).hexdigest()
    username = request.form["Username"]
    
    if request.form["action"] == "Register":
        if login.register(username, password):
            text = "Register Successful"
        else:
            text = "Username Exists Already"
        return render_template('form.html', text = text)

    elif request.form["action"] == "Login":
        if login.login(username, password):
            session["Username"] = username
            return redirect(url_for('mainPage'))    
        else:
            return render_template('form.html', text = "Login Failed")

@app.route("/")
def mainPage():
    if not "Username" in session:
        return redirect(url_for('getForm'))
    return render_template('main.html', name = session["Username"])    
            
@app.route("/logout/")
def logout():
    if "Username" in session:
        session.pop("Username")
        return redirect(url_for('getForm'))
    return redirect(url_for('getForm'))    
    

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
