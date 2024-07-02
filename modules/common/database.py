import sqlite3
# from sqlite3 import Error


# Task 5 Compulsory Part
class Database:

    def __init__(self) -> None:
        self.connection = sqlite3.connect(r"become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Databese Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT id, name, address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Additional Part Begins

    # Method trys to insert a new customer into database
    def try_insert_new_customer(
        self,
        new_customer_id,
        new_customer_name,
        new_customer_address,
        new_customer_city,
        new_customer_postalCode,
        new_customer_country,
    ):
        try:
            query = f"""INSERT INTO customers (id, name, address, city, postalCode, country) \
                                 VALUES ({new_customer_id}, '{new_customer_name}', '{new_customer_address}', '{new_customer_city}', '{new_customer_postalCode}', '{new_customer_country}')"""
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error inserting customer: {e}")

    # Metod to update customer data
    def update_user_data_by_id(
        self,
        updated_customer_name,
        updated_customer_address,
        updated_customer_city,
        updated_customer_postalCode,
        updated_customer_country,
        customer_id_to_update,
    ):
        query = f"UPDATE customers SET  name = '{updated_customer_name}', \
                                        address = '{updated_customer_address}', \
                                        city = '{updated_customer_city}', \
                                        postalCode = '{updated_customer_postalCode}', \
                                        country = '{updated_customer_country}' \
                                    WHERE id = {customer_id_to_update}"
        self.cursor.execute(query)
        self.connection.commit()

    # Method to get user data by id
    def get_customer_data_by_id(self, customer_id):
        query = f"SELECT id, name, address, city, postalCode, country FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Metod to determine customer ID to insert
    def get_next_empty_raw_at_customers(self):
        query = "SELECT MAX(id) FROM customers"
        self.cursor.execute(query)
        max_id = self.cursor.fetchone()[0]
        if max_id is None:
            return 1  # If no rows exist, start from 1
        else:
            return max_id + 1

    # Method to delete a customer
    def delete_customer_by_id(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

