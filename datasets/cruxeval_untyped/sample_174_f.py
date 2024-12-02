def f(lst):
    """"""
    ### Canonical solution below ###
    lst[1:4] = lst[1:4][::-1]
    return lst

def check(candidate):
    assert candidate([1, 2, 3]) == [1, 3, 2]

def test_check():
	check(f)