def f(s, from_c, to_c):
    """"""
    ### Canonical solution below ###
    table = s.maketrans(from_c, to_c)
    return s.translate(table)

def check(candidate):
    assert candidate('aphid', 'i', '?') == 'aph?d'

def test_check():
	check(f)