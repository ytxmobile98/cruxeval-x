def f(text):
    """"""
    ### Canonical solution below ###
    if text.isdecimal():
        return 'yes'
    else:
        return 'no'

def check(candidate):
    assert candidate("abc") == 'no'

def test_check():
	check(f)