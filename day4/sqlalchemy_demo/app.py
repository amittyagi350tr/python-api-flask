from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Employee, Project

##create a database

db_name = "records.db"

#### how to connect to different kinds of databases?

## a) SQLITE

url = f"sqlite:///{db_name}"

#engine : a variable that stores connection details
engine = create_engine(url)

#### Base knows how many models are to be created
#all tables will be created automatically now
Base.metadata.create_all(engine)

#since engine has credentials for connection stored, initiate a session
Session_Class = sessionmaker(bind=engine) #Session class

#session variable: object of Session
session = Session_Class()

e1 = Employee(eid=101,name="Harshit", age=32, location="Mumbai", salary=40000)
e2 = Employee(eid=202,name="Shreyanshi",age = 31, location="Bengaluru", salary=50000)
p1 = Project(pid=1111, name="API development")

#notice how add_all performed (INSERT INTO TABLE NAME QUERY automatically)
session.add_all([e1,e2,p1])



session.commit()


"""

step 1: user interacts with front-end UI(web-page or app screen)
step 2: we capture data from the user and send it to the API layer
    (user-data--->JSON---->python_object)[   job of API   ]
step 3: PYTHON data is translated by SQL Alchemy into SQL rows
        BASED ON SOME REFERENCE SCHEMA (implemented as a class in python)
step 4: data reaches SQL database table as a SQL row
"""