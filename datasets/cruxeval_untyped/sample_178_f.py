def f(array, n):
    """"""
    ### Canonical solution below ###
    return array[n:]

def check(candidate):
    assert candidate([0, 0, 1, 2, 2, 2, 2], 4) == [2, 2, 2]

def test_check():
	check(f)