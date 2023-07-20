from sqlalchemy import Column, Integer, String, SmallInteger, Date, REAL
from sqlalchemy.ext.declarative import declarative_base


BASE = declarative_base()

class Order(BASE):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, nullable=False)
    customer_id = Column(String(16), nullable=True)
    employee_id = Column(SmallInteger, nullable=True)
    order_date = Column(Date, nullable=True)
    required_date = Column(Date, nullable=True)
    shipped_date = Column(Date, nullable=True)
    ship_via = Column(SmallInteger)
    freight = Column(REAL)
    ship_name = Column(String(40))
    ship_address = Column(String(60))
    ship_city = Column(String(15))


class Customer(BASE):
    __tablename__ = 'customers'

    customer_id = Column(String, primary_key=True)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))


class Employee(BASE):
    __tablename__ = 'employees'

    employee_id = Column(SmallInteger, primary_key=True)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(10), nullable=False)
    title = Column(String(30))
    country = Column(String(15))