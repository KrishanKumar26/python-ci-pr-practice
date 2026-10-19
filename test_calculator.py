from calculator import add


def test_both_numbers_greater_than_10():
    assert add(11, 12) == 33


def test_both_numbers_less_than_10():
    assert add(2, 3) == 10


def test_mixed_numbers():
    assert add(11, 2) == 13


def test_both_numbers_equal_to_10():
    assert add(10, 10) == 20
