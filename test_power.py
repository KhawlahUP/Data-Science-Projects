from calculator import power


def test_power():
    results = power(4, 2)
    assert results == 16

    results = power(3, 3)
    assert results == 27