from flask import Flask, render_template, request, session
from utils import login
import hashlib

app = Flask(__name__)
session["Logged In"] = False

@app.route("/login")
def getForm():
    if session["Logged In"]
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
        return render_template('form.html' text = text)

    elif request.form["action"] == "Login":
        if login.login(username, password):
            session["Logged In"] = True
            session["Username"] = username
            return redirect(url_for('mainPage'))    
        else:
            return render_template('form.html' text = "Login Failed")

@app.route("/")
def mainPage():
    if !session["Logged In"]
        redirect(url_for('getForm'))
    return render_template('main.html')    
            
    
        
    

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
