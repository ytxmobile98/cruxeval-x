def f(lst, i, n):
    """"""
    ### Canonical solution below ###
    lst.insert(i, n)
    return lst

def check(candidate):
    assert candidate([44, 34, 23, 82, 24, 11, 63, 99], 4, 15) == [44, 34, 23, 82, 15, 24, 11, 63, 99]

def test_check():
	check(f)