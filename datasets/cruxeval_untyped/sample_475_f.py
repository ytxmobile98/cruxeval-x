def f(array, index):
    """"""
    ### Canonical solution below ###
    if index < 0:
        index = len(array) + index
    return array[index]

def check(candidate):
    assert candidate([1], 0) == 1

def test_check():
	check(f)