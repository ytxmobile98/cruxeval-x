def f(array):
    """"""
    ### Canonical solution below ###
    while -1 in array:
        array.pop(-3)
    while 0 in array:
        array.pop()
    while 1 in array:
        array.pop(0)
    return array

def check(candidate):
    assert candidate([0, 2]) == []

def test_check():
	check(f)