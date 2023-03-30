#from flask library, import class named as "Flask"
from flask import Flask

app = Flask(__name__) #__name__ stores the name of currently executing .py file


@app.route("/", methods=["GET"])
def hello():
    page = "<h1> Hello,World </h1>"    
    return page


@app.route("/info", methods=["GET"])
def info():
    return "INFO PAGE REACHED"


app.run()




