from flask import Flask,render_template
import  pandas as pd
app = Flask(__name__)


@app.route('/base/')
@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route('/NLG/')
def NLG():
    return render_template("index4.html")


@app.route("/getdata/")
def GetData():
    return "HELLO WORLD.THIS IS DATA FROM BACKEND"

if __name__ == '__main__':
    app.run(debug=True)
