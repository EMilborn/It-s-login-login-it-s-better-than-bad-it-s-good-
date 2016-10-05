from flask import Flask, render_template, request
from login import register, login
import hashlib

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def getForm():
    return render_template('form.html',
                           name01 = "Username",
                           name02 = "Password",
                           heading01 = "LOGIN",
                           name03 = "R/L",
                           name04 = "Register",
                           name05 = "Login")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    winOrLose = "ERROR"
    password = hashlib.sha256(request.form["Password"]).hexdigest()
    username = request.form("Username")
    
    if request.form["R/L"] == "Register":
        if login.register(username, password):
            winOrLose = "Register Successful"
        else:
            winOrLose = "Register Failed"

    elif request.form["R/L"] == "Login":
        if login.login(username, password):
            winOrLose = "Login Successful"
        else:
            winOrLose = "Login Failed"

    return render_template('authenticate.html',
                           text = winOrLose)
            
    
        
    

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
