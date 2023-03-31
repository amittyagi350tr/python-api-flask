from models import Employee, app, db

from flask import Response, render_template, redirect, url_for, request, jsonify

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
if __name__=="__main__":
    app.run()


