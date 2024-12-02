def f(text, value):
    """"""
    ### Canonical solution below ###
    return text.ljust(len(value), "?")

def check(candidate):
    assert candidate("!?", "") == '!?'

def test_check():
	check(f)