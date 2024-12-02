def f(lst):
    """"""
    ### Canonical solution below ###
    lst.sort()
    return lst[0:3]

def check(candidate):
    assert candidate([5, 8, 1, 3, 0]) == [0, 1, 3]

def test_check():
	check(f)