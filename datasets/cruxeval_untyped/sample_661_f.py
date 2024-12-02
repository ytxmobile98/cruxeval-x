def f(letters, maxsplit):
    """"""
    ### Canonical solution below ###
    return ''.join(letters.split()[-maxsplit:])

def check(candidate):
    assert candidate('elrts,SS ee', 6) == 'elrts,SSee'

def test_check():
	check(f)