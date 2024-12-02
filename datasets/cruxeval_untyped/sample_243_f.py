def f(text, char):
    """"""
    ### Canonical solution below ###
    return char.islower() and text.islower()

def check(candidate):
    assert candidate('abc', 'e') == True

def test_check():
	check(f)