#from flask library, import class named as "Flask"
from flask import Flask,render_template

app = Flask(__name__) #__name__ stores the name of currently executing .py file


@app.route("/", methods=["GET"])
def hello():
    return render_template("landing.html")

@app.route("/info", methods=["GET"])
def info():
    return render_template("info.html")


@app.route("/data", methods=["GET"]) #user can go to /data and fetch information. We can't take user data and put in backend here
def display_data():
    return [1,28, "Harshit", 32, ["IT","Python"]]

#alternate way of making a GET REST API
@app.get("/result")
def dislay_result():
    return "result display"


"""
    if name of the currently executing script is matches with the name of this file i.e if we are running this script
    as our main file, do whatever is written inside
"""
if __name__ == "__main__":
    app.run(debug=True)
