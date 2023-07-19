insert_query = """
    INSERT INTO orders(customer_id, employee_id, order_date)
    VALUES (%(customer_id)s, %(employee_id)s, CURRENT_DATE)
"""

delete_query = """
    DELETE FROM orders
    WHERE customer_id = %(customer_id)s AND employee_id = %(employee_id)s
"""

select_query = """
    SELECT * FROM orders
    WHERE customer_id = %(customer_id)s AND employee_id = %(employee_id)s
"""

count_query = """
    SELECT COUNT(*) FROM orders
    WHERE customer_id = %(customer_id)s AND employee_id = %(employee_id)s
"""

long_select_with_joins_query = """
    SELECT customers.contact_name, COUNT(orders.order_id) AS orders, COUNT(employees.employee_id) AS employee
    FROM customers
    JOIN orders USING(customer_id)
    JOIN employees USING(employee_id)
    GROUP BY contact_name, employee_id
    ORDER BY COUNT(orders.order_id);
"""

update_query = """
    UPDATE orders
    SET customer_id = %(new_customer)s, employee_id = %(new_employee)s
    WHERE customer_id = %(customer_id)s AND employee_id = %(employee_id)s
"""