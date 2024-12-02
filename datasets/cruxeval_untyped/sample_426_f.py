def f(numbers, elem, idx):
    """"""
    ### Canonical solution below ###
    numbers.insert(idx, elem)
    return numbers

def check(candidate):
    assert candidate([1, 2, 3], 8, 5) == [1, 2, 3, 8]

def test_check():
	check(f)