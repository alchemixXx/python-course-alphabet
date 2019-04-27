from typing import List


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    with con.cursor() as cur:
        cur.execute("""INSERT INTO 
        customers(customername, contactname, address, city, postalcode, country) 
        VALUES 
        ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');
        SELECT * FROM customers;""")
        return cur.fetchall()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("""SELECT * FROM Customers 
                   WHERE country = 'Germany'""")
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    with con.cursor() as cur:
        cur.execute("""UPDATE customers 
                       SET customername = 'Johnny Depp' WHERE customerid = 1;
                       SELECT * FROM customers""")
        return cur.fetchall()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cur:
        cur.execute("""DELETE FROM customers 
                       WHERE customerid = (SELECT MAX(customerid) 
                       FROM customers)""")


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("""SELECT country FROM suppliers;""")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("""SELECT country FROM suppliers 
                   ORDER BY country DESC ;""")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    # cur.execute("""SELECT city, COUNT(city) FROM customers GROUP BY city;""")
    cur.execute("""SELECT city, COUNT(DISTINCT city) 
                   FROM customers GROUP BY city;""")
    x = cur.fetchall()
    # print(x)
    return x
    # return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("""SELECT COUNT(country), country 
                FROM customers 
                GROUP BY country 
                HAVING COUNT(country) > 10
                ORDER BY COUNT(country) DESC,
                country;""")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("""SELECT * FROM customers LIMIT 10;""")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("""SELECT * FROM customers OFFSET 11;""")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute("""SELECT supplierid, suppliername, contactname, city, country
                   FROM suppliers 
                   WHERE country in ('USA', 'UK', 'Japan')
                   ORDER BY supplierid;""")
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("""SELECT productname 
                   FROM products 
                   WHERE supplierid 
                   IN (SELECT suppliers.supplierid FROM suppliers WHERE country = 'Sweden')""")
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute("""SELECT products.productid, products.productname, products.unit, products.price, suppliers.country, suppliers.city, suppliers.suppliername  
                   FROM products 
                   LEFT JOIN suppliers 
                   ON products.supplierid = suppliers.supplierid """)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute("""SELECT customers.customername, customers.contactname, customers.country, orders.orderid
                   FROM customers 
                   LEFT JOIN orders
                   ON customers.customerid = orders.customerid
                   ORDER BY orders.orderid
                   """)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute("""SELECT customers.customername customername,
                   customers.address address,
                   customers.country customercountry,
                   suppliers.country suppliercountry, 
                   suppliers.suppliername suppliername
                   FROM customers 
                   FULL OUTER JOIN suppliers
                   ON customers.country = suppliers.country
                   ORDER BY customercountry,
                   suppliercountry;
                   """)
    return cur.fetchall()
