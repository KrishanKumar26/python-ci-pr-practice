def validate_customer(customer):
    if not customer.get("name"):
        return False

    if customer.get("age", 0) <= 0:
        return False

    return True


def filter_valid_customers(customers):
    return [
        customer
        for customer in customers
        if validate_customer(customer)
    ]
