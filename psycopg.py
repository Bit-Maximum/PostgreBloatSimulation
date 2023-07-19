import psycopg2
from queries import insert_query, delete_query, select_query, count_query, long_select_with_joins_query, update_query

# Import secrets
import os
from dotenv import load_dotenv, find_dotenv

import time


def create_connection(db_name, db_user, db_password, db_host, db_port=5432):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f"Connection to {db_name} successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def get_bloat_query(db_connection):
    db_connection.autocommit = True
    with db_connection.cursor() as cursor:
        for _ in range(50):
            cursor.execute(insert_query, {'customer_id': 'ERNSH', 'employee_id': 1})
            cursor.execute(insert_query, {'customer_id': 'ERNSH', 'employee_id': 1})
            cursor.execute(insert_query, {'customer_id': 'LEHMS', 'employee_id': 2})
            time.sleep(0.15)

        cursor.execute(delete_query, {'customer_id': 'LEHMS', 'employee_id': 2})
        for _ in range(50):
            cursor.execute(insert_query, {'customer_id': 'LEHMS', 'employee_id': 2})
            cursor.execute(insert_query, {'customer_id': 'ERNSH', 'employee_id': 1})
            cursor.execute(insert_query, {'customer_id': 'LEHMS', 'employee_id': 2})
            time.sleep(0.15)

        start = time.time()
        cursor.execute(select_query, {'customer_id': 'ERNSH', 'employee_id': 1})
        end = time.time() - start
        print(f"\nSELECT time: {end}\n")
        start = time.time()
        cursor.execute(count_query, {'customer_id': 'ERNSH', 'employee_id': 1})
        end = time.time() - start
        print(f"\nCOUNT time: {end}\n")
        print(cursor.fetchall())
        cursor.execute(update_query, {'new_customer': 'LEHMS', 'new_employee': 2,
                                     'customer_id': 'ERNSH', 'employee_id': 1})

        time.sleep(0.5)
        cursor.execute(long_select_with_joins_query)
        print(cursor.fetchall())
        cursor.execute(delete_query, {'customer_id': 'LEHMS', 'employee_id': 2})

        time.sleep(0.5)
        cursor.execute(delete_query, {'customer_id': 'LEHMS', 'employee_id': 2})
        cursor.execute(delete_query, {'customer_id': 'ERNSH', 'employee_id': 1})


if __name__ == "__main__":
    # Import secrets from venv
    load_dotenv(r"venv/.env")

    connection = create_connection(
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST")
    )
    try:
        while True:
            get_bloat_query(connection)
            time.sleep(3)
            print("\n\nCYCLE NOTIFICATION\n\n")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")




