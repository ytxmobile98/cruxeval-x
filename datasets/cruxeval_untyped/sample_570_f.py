def f(array, index, value):
    """"""
    ### Canonical solution below ###
    array.insert(0, index + 1)
    if value >= 1:
        array.insert(index, value)
    return array

def check(candidate):
    assert candidate([2], 0, 2) == [2, 1, 2]

def test_check():
	check(f)