def f(s):
    """"""
    ### Canonical solution below ###
    while len(s) > 1:
        s.clear()
        s.append(len(s))
    return s.pop()

def check(candidate):
    assert candidate([6, 1, 2, 3]) == 0

def test_check():
	check(f)