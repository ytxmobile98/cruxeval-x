def f(s, tab):
    """"""
    ### Canonical solution below ###
    return s.expandtabs(tab)

def check(candidate):
    assert candidate("Join us in Hungary", 4) == 'Join us in Hungary'

def test_check():
	check(f)