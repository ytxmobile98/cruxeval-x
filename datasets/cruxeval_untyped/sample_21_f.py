def f(array):
    """"""
    ### Canonical solution below ###
    n = array.pop()
    array.extend([n, n])
    return array

def check(candidate):
    assert candidate([1, 1, 2, 2]) == [1, 1, 2, 2, 2]

def test_check():
	check(f)