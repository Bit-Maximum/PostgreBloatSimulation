from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from AlchemyTables import Order, Employee, Customer

# Import secrets
import os
from dotenv import load_dotenv

import time


if __name__ == "__main__":
    # Import secrets from venv
    load_dotenv(r"venv/.env")

    engine = create_engine(
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}",
        echo=True
    )
    session = sessionmaker(bind=engine)
    s = session()
    while True:
        for _ in range(50):
            temp_order = Order(customer_id="ERNSH", employee_id=1)
            s.add(temp_order)
            s.commit()
            temp_order = Order(customer_id="ERNSH", employee_id=1)
            s.add(temp_order)
            s.commit()
            temp_order = Order(customer_id="LEHMS", employee_id=2)
            s.add(temp_order)
            s.commit()

        s.delete(s.query(Order).filter(Order.customer_id == 'LEHMS').filter(Order.employee_id == 2))

        for _ in range(50):
            s.add_all([Order(customer_id="ERNSH", employee_id=1),
                       Order(customer_id="LEHMS", employee_id=2),
                       Order(customer_id="ERNSH", employee_id=1)])
            s.commit()

        for row in s.query(Order).filter(Order.customer_id == 'LEHMS').filter(Order.employee_id == 2).all():
            print(row)

        print(s.query(Order).filter(Order.customer_id == 'LEHMS').filter(Order.employee_id == 2).count())

        temp_update = s.query(Order).filter(Order.customer_id == 'ERNSH').filter(Order.employee_id == 1).first()
        if temp_update:
            temp_update.customer_id = "LEHMS"
            temp_update.employee_id = 2
            s.add(temp_update)
            s.commit()
        time.sleep(0.5)

        print([(row.Customer.contact_name, row.Order.order_id.count()) for row in s.query(Order, Customer, Employee).filter(Order.customer_id == Customer.customer_id).filter(Order.employee_id == Employee.employee_id).group_by(Customer.contact_name, Order.employee_id).order_by(Order.order_id.count())])
        s.delete(s.query(Order).filter(Order.customer_id == 'LEHMS').filter(Order.employee_id == 2))
        s.delete(s.query(Order).filter(Order.customer_id == 'ERNSH').filter(Order.employee_id == 1))
        time.sleep(3)
        print("\n\nCYCLE NOTIFICATION\n\n")