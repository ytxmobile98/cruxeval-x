def f(a, b):
    """"""
    ### Canonical solution below ###
    a.sort()
    b.sort(reverse=True)
    return a + b

def check(candidate):
    assert candidate([666], []) == [666]

def test_check():
	check(f)