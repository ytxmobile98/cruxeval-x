def f(match, fill, n):
    """"""
    ### Canonical solution below ###
    return fill[:n] + match

def check(candidate):
    assert candidate('9', '8', 2) == '89'

def test_check():
	check(f)