def f(m):
    """"""
    ### Canonical solution below ###
    m.reverse()
    return m

def check(candidate):
    assert candidate([-4, 6, 0, 4, -7, 2, -1]) == [-1, 2, -7, 4, 0, 6, -4]

def test_check():
	check(f)