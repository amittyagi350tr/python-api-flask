from models import Employee, User, app, db

from flask import Response, flash, render_template, redirect, url_for, request, jsonify

from werkzeug.security import generate_password_hash, check_password_hash

@app.get("/")
def landing_page():
    return render_template("landing.html")


@app.get("/details")
def display_employee_records():

    results = Employee.query.all() #select * from Employee
    return jsonify(   [emp for emp in results  ]     )


@app.get("/employee")
def show_employee_creation_form():

    return render_template("create_employee.html")

@app.post("/employee")
def add_employee_record():

    #data means all input data received as a JSON from front-end
    
    eid = request.form["eid"]
    ename = request.form["ename"]
    eage = request.form["eage"]
    
    #make a python object based on separated fields
    emp = Employee(eid=eid, ename=ename, eage=eage)

    #let SQLAlchemy convert python object to SQL row
    db.session.add(emp)
    db.session.commit()

    return Response(status=200)

@app.delete("/erase")
def delete_employee_by_eid():
    eid = request.args.get("eid")

    #fetch records from Employee with eid equal to whatever user has mentioned
    #select * from Employee where eid = 101 LIMIT 1
    emp = Employee.query.filter_by(eid=eid).first()
    if emp is None:
        return jsonify( {"msg" : f"Employee with id {eid} not found"}  )
    else:
        db.session.delete(emp)
        db.session.commit()

    return Response(status=200)


@app.get("/erase")
def show_delete_form():
    return render_template("delete_employee.html")



@app.route("/user", methods=["GET","POST"])
def create_user():
    #request.json or request.form
    if request.method == "POST":
       name=request.form["name"]
       age=request.form["age"]
       email=request.form["email"]
       password=request.form["password"]
       user = User(name=name, age=age, email=email, password=generate_password_hash(password))
       db.session.add(user)
       db.session.commit()
       return Response(status=200)

    if request.method=="GET":
        return render_template("register_employee.html")    
    
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        email  = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email = email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("LOGGED IN SUCCESSFULLY!", category="sucess")
            else:
                flash("LOGIN FAILED. TRY AGAIN!", category="error")
        else:
            flash("USER ACCOUNT with this ID does not exist")

    return redirect(url_for("landing_page"))
if __name__=="__main__":
    app.run()


## 8779092028
## harshitshukla36@gmail.com