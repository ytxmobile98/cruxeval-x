def f(text):
    """"""
    ### Canonical solution below ###
    if text.isascii():
        return 'ascii'
    else:
        return 'non ascii'

def check(candidate):
    assert candidate("<<<<") == 'ascii'

def test_check():
	check(f)