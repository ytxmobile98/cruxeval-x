def f(array, elem):
    """"""
    ### Canonical solution below ###
    if elem in array:
        return array.index(elem)
    return -1

def check(candidate):
    assert candidate([6, 2, 7, 1], 6) == 0

def test_check():
	check(f)