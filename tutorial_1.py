from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("index1.html")
    else:
        info()
        return redirect(url_for("info"))
    
@app.route("/info",methods = ["POST"])    
def info():
    global name,email
    name = request.form.get("Nameinput")
    email = request.form.get("passwordInput")
    print(name + email)
    return render_template('index2.html',username=name,password=email)
    
if __name__ == "__main__":
    app.run()
