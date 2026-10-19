from pipeline import validate_customer, filter_valid_customers


def test_valid_customer():
    customer = {"name": "Krish", "age": 21}
    assert validate_customer(customer) is True


def test_customer_without_name():
    customer = {"age": 21}
    assert validate_customer(customer) is False


def test_customer_with_invalid_age():
    customer = {"name": "Krish", "age": 0}
    assert validate_customer(customer) is False


def test_filter_valid_customers():
    customers = [
        {"name": "Krish", "age": 21},
        {"name": "", "age": 22},
        {"name": "Rahul", "age": 25},
    ]

    result = filter_valid_customers(customers)

    assert len(result) == 2
