def f(s, l):
    """"""
    ### Canonical solution below ###
    return s.ljust(l, '=').rpartition('=')[0]

def check(candidate):
    assert candidate('urecord', 8) == 'urecord'

def test_check():
	check(f)