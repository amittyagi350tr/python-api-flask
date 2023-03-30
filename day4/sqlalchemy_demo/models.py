from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):

    __tablename__ = "Employee"  

    employee_id = Column("employee_id", Integer, primary_key=True)
    employee_name = Column("employee_name", String)
    employee_age = Column("employee_age", Integer)
    employee_location = Column("employee_location", String)
    employee_salary=Column("employee_salary", Integer)

    def __init__(self,eid,name, age, location, salary) -> None:
        self.employee_id=eid
        self.employee_name = name
        self.employee_age = age
        self.employee_location = location
        self.employee_salary=salary

    def __repr__(self) -> str:
        return f"{self.__dict__}"
    

class Project(Base):

    __tablename__ = "Project"  

    project_id = Column("project_id", Integer, primary_key=True)
    project_name = Column("project_name", String)
  
    def __init__(self,pid,name) -> None:
        self.project_id=pid
        self.project_name = name
  
    def __repr__(self) -> str:
        return f"{self.__dict__}"