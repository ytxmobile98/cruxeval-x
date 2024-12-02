def f(text, delim):
    """"""
    ### Canonical solution below ###
    return text[:text[::-1].find(delim)][::-1]

def check(candidate):
    assert candidate('dsj osq wi w', ' ') == 'd'

def test_check():
	check(f)