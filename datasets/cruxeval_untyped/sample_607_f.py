def f(text):
    """"""
    ### Canonical solution below ###
    for i in ['.', '!', '?']:
        if text.endswith(i):
            return True
    return False

def check(candidate):
    assert candidate('. C.') == True

def test_check():
	check(f)