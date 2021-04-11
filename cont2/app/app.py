from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is container 2."

@app.route("/invert/<txt>")
def inverter(txt):
    return txt[::-1]

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")