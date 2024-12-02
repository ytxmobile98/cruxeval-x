def f(challenge):
    """"""
    ### Canonical solution below ###
    return challenge.casefold().replace('l', ',')

def check(candidate):
    assert candidate('czywZ') == 'czywz'

def test_check():
	check(f)