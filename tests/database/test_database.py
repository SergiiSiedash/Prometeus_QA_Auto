import pytest
import sqlite3
from sqlite3 import OperationalError

# Task 5 Compulsory Part
"""Parameter database was added wich refers to fixture \
    in order to remove reusing of db = Database() object"""


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4, "печиво", "солодке", 30)
    water_qnt = database.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, "тестові", "дані", 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення", orders)

    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Task 5 Additional Part Begins
"""Additional part tests for database testing \
    Tests are marked as db_additional"""


# Test that user with correct data is sucsessfully added
@pytest.mark.db_additional
def test_new_customer_insert(database):
    new_customer_id = 3
    new_customer_name = "Sam"
    new_customer_address = "11 Doroshenka str"
    new_customer_city = "Zhaskiv"
    new_customer_postalCode = "8ABC"
    new_customer_country = "Mars"

    database.try_insert_new_customer(
        new_customer_id,
        new_customer_name,
        new_customer_address,
        new_customer_city,
        new_customer_postalCode,
        new_customer_country,
    )

    new_customer = database.get_customer_data_by_id(customer_id=new_customer_id)

    # Check structure of data
    assert new_customer[0][0] == new_customer_id
    assert new_customer[0][1] == new_customer_name
    assert new_customer[0][2] == new_customer_address
    assert new_customer[0][3] == new_customer_city
    assert new_customer[0][4] == new_customer_postalCode
    assert new_customer[0][5] == new_customer_country
    print(new_customer)


# Test that customer data are sucsessfully updated
@pytest.mark.db_additional
def test_customer_data_update(database):

    customer_id_to_update = 3
    updated_customer_name = "Anton"
    updated_customer_address = "1000 Nova str."
    updated_customer_city = "Fridrichshaffen"
    updated_customer_postalCode = "W321W"
    updated_customer_country = "Mercury"

    database.update_user_data_by_id(
        updated_customer_name,
        updated_customer_address,
        updated_customer_city,
        updated_customer_postalCode,
        updated_customer_country,
        customer_id_to_update,
    )
    updated_customer_data = database.get_customer_data_by_id(
        customer_id=customer_id_to_update
    )

    # Check structure of data
    assert updated_customer_data[0][0] == customer_id_to_update
    assert updated_customer_data[0][1] == updated_customer_name
    assert updated_customer_data[0][2] == updated_customer_address
    assert updated_customer_data[0][3] == updated_customer_city
    assert updated_customer_data[0][4] == updated_customer_postalCode
    assert updated_customer_data[0][5] == updated_customer_country


# Test that customer deleted
@pytest.mark.db_additional
def test_customer_deleted(database):
    customer_id_to_delete = 3
    database.delete_customer_by_id(customer_id=customer_id_to_delete)
    deleted_customer_data = database.get_customer_data_by_id(
        customer_id=customer_id_to_delete
    )
    assert len(deleted_customer_data) == 0
