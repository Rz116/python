from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("index1.html")
    else:
        Getinfo()
        return render_template("index1.html")
    
def Getinfo():
    name = request.form.get("Nameinput")
    email = request.form.get("MailInput")
    print("Hello " + name + " Thank you for your email: " + email)
    
if __name__ == "__main__":
    app.run()
