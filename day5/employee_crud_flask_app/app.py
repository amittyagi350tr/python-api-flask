from models import Employee, app, db

from flask import render_template, redirect, url_for, request, jsonify

@app.get("/")
def landing_page():
    return render_template("landing.html")


@app.get("/employee")
def display_employee_records():
    #find entries from SQL table<---->make them python_objects
    #manipulate received data, transform, process and prepare for it for the user
    #send all python_objects on to the HTML front-end (flask should convert your
    # objects into JSON)

    results = Employee.query.all() #select * from Employee
    return jsonify(results)


"""   
          json_object
    user ------->             API(request can access input json_object)

"""

@app.post("/employee")
def add_employee_record():

    #data means all input data received as a JSON from front-end
    data = request.get_json()

    #separate out all json fields
    eid=data["eid"]
    ename=data["ename"]
    eage=data["eage"]
    
    #make a python object based on separated fields
    emp = Employee(eid=eid, ename=ename, eage=eage)

    #let SQLAlchemy convert python object to SQL row
    db.session.add(emp)
    db.session.commit()

if __name__=="__main__":
    app.run()