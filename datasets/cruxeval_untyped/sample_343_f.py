def f(array, elem):
    """"""
    ### Canonical solution below ###
    array.extend(elem)
    return array

def check(candidate):
    assert candidate([[1, 2, 3], [1, 2], 1], [[1, 2, 3], 3, [2, 1]]) == [[1, 2, 3], [1, 2], 1, [1, 2, 3], 3, [2, 1]]

def test_check():
	check(f)