def f(values):
    """"""
    ### Canonical solution below ###
    values.sort()
    return values

def check(candidate):
    assert candidate([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_check():
	check(f)