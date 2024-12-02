def f(lst):
    """"""
    ### Canonical solution below ###
    lst.clear()
    for i in lst:
        if i == 3:
            return False
    else:
        return True

def check(candidate):
    assert candidate([2, 0]) == True

def test_check():
	check(f)