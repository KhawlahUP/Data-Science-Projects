from calculator import divide


def test_divide():
    results = divide(12, 3)
    assert results == 4


def test_divide_by_zero():
    results = divide(66, 0)
    assert type(results) == str