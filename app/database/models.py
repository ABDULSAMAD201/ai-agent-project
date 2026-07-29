from sqlalchemy import Column, Integer, String

from app.database.connection import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    department_id = Column(Integer)

    salary = Column(Integer)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    department_id = Column(Integer)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    city = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    price = Column(Integer)

class CustomerOrder(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer)

    product_id = Column(Integer)

    quantity = Column(Integer)

    order_date = Column(String)