from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def getForm():
    return render_template('form.html',
                           name01 = "Username",
                           name02 = "Password",
                           heading01 = "LOGIN")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    if request.form["Username"] == "Dyrland" and request.form["Password"] == "Weaver":
        return "Hi Mr. DW!!!"
    return "Who are you??"

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
