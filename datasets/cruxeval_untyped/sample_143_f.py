def f(s, n):
    """"""
    ### Canonical solution below ###
    return s.casefold() == n.casefold()

def check(candidate):
    assert candidate("daaX", "daaX") == True

def test_check():
	check(f)