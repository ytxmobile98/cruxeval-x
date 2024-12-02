def f(text, lower, upper):
    """"""
    ### Canonical solution below ###
    return text[lower:upper].isascii()

def check(candidate):
    assert candidate('=xtanp|sugv?z', 3, 6) == True

def test_check():
	check(f)