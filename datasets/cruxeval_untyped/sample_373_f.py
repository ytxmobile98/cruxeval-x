def f(orig):
    """"""
    ### Canonical solution below ###
    copy = orig
    copy.append(100)
    orig.pop()
    return copy

def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]

def test_check():
	check(f)