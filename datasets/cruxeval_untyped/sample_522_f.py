def f(numbers):
    """"""
    ### Canonical solution below ###
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []

def check(candidate):
    assert candidate(range(100, 120)) == []

def test_check():
	check(f)