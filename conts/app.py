from flask import Flask
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return "Here be call to Cont2"
@app.route("/noparam/")
def compose_test():
    try:
        txt = requests.get("http://cont2:5000").text
    except:  
        txt = "Connection to cont2 failed"
    return txt  


@app.route("/pars/<param>")
def call_with_param(param):
    r = requests.get("http://cont2:5000/invert/" + param)
    if r.status_code != 200:
        return "Call to Cont2 failed"
    else:
        return "Cont2 returned: <i>" + r.text + "</i>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


