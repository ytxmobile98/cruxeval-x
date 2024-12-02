def f(text):
    """"""
    ### Canonical solution below ###
    return not any([c.isupper() for c in text])

def check(candidate):
    assert candidate('lunabotics') == True

def test_check():
	check(f)