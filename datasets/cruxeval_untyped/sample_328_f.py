def f(array, L):
    """"""
    ### Canonical solution below ###
    if L <= 0:
        return array
    if len(array) < L:
        array.extend(f(array, L - len(array)))
    return array

def check(candidate):
    assert candidate([1, 2, 3], 4) == [1, 2, 3, 1, 2, 3]

def test_check():
	check(f)