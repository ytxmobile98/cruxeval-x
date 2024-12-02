def f(array):
    """"""
    ### Canonical solution below ###
    l = len(array)
    if l % 2 == 0:
        array.clear()
    else:
        array.reverse()
    return array

def check(candidate):
    assert candidate([]) == []

def test_check():
	check(f)