import addition

def test_add_numbers():
    assert addition.add_numbers(2, 3) == 5
    assert addition.add_numbers(-1, 1) == 0
    assert addition.add_numbers(0, 0) == 0
    assert addition.add_numbers(10, -5) == 5
