def f(array):
    """"""
    ### Canonical solution below ###
    new_array = array.copy()
    new_array = reversed(new_array)
    return [x*x for x in new_array]

def check(candidate):
    assert candidate([1, 2, 1]) == [1, 4, 1]

def test_check():
	check(f)