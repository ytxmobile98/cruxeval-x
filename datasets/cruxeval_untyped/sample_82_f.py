def f(a, b, c, d):
    """"""
    ### Canonical solution below ###
    return a and b or c and d

def check(candidate):
    assert candidate('CJU', 'BFS', 'WBYDZPVES', 'Y') == 'BFS'

def test_check():
	check(f)