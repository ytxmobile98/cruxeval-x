def f(s):
    """"""
    ### Canonical solution below ###
    return ''.join((c.casefold() for c in s))

def check(candidate):
    assert candidate('abcDEFGhIJ') == 'abcdefghij'

def test_check():
	check(f)