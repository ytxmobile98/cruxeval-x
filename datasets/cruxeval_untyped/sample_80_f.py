def f(s):
    """"""
    ### Canonical solution below ###
    return ''.join(reversed(s.rstrip()))

def check(candidate):
    assert candidate('ab        ') == 'ba'

def test_check():
	check(f)