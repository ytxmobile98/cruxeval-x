def f(array, elem):
    """"""
    ### Canonical solution below ###
    return array.count(elem) + elem

def check(candidate):
    assert candidate([1, 1, 1], -2) == -2

def test_check():
	check(f)