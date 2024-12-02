def f(length, text):
    """"""
    ### Canonical solution below ###
    if len(text) == length:
        return text[::-1]
    return False

def check(candidate):
    assert candidate(-5, 'G5ogb6f,c7e.EMm') == False

def test_check():
	check(f)