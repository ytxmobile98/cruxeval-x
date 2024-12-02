def f(s, c):
    """"""
    ### Canonical solution below ###
    s = s.split(' ')
    return ((c + "  ") + ("  ".join(s[::-1])))

def check(candidate):
    assert candidate('Hello There', '*') == '*  There  Hello'

def test_check():
	check(f)