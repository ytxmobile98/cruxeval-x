def f(t):
    """"""
    ### Canonical solution below ###
    for c in t:
        if not c.isnumeric():
            return False
    return True

def check(candidate):
    assert candidate('#284376598') == False

def test_check():
	check(f)