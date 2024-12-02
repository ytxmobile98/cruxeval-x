def f(s, sep):
    """"""
    ### Canonical solution below ###
    reverse = ['*' + e for e in s.split(sep)]
    return ';'.join(reversed(reverse))

def check(candidate):
    assert candidate('volume', 'l') == '*ume;*vo'

def test_check():
	check(f)