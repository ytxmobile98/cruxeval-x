def f(text):
    """"""
    ### Canonical solution below ###
    for char in text:
        if not char.isspace():
            return False
    return True

def check(candidate):
    assert candidate('     i') == False

def test_check():
	check(f)