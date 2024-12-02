def f(array, elem):
    """"""
    ### Canonical solution below ###
    array.reverse()
    try:
        found = array.index(elem)
    finally:
        array.reverse()
    return found

def check(candidate):
    assert candidate([5, -3, 3, 2], 2) == 0

def test_check():
	check(f)