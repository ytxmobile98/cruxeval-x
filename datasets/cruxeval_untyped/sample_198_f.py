def f(text, strip_chars):
    """"""
    ### Canonical solution below ###
    return text[::-1].strip(strip_chars)[::-1]

def check(candidate):
    assert candidate('tcmfsmj', 'cfj') == 'tcmfsm'

def test_check():
	check(f)