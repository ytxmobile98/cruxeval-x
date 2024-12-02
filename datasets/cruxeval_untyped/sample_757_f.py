def f(text, char, replace):
    """"""
    ### Canonical solution below ###
    return text.replace(char, replace)

def check(candidate):
    assert candidate('a1a8', '1', 'n2') == 'an2a8'

def test_check():
	check(f)