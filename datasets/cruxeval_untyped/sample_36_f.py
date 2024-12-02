def f(text, chars):
    """"""
    ### Canonical solution below ###
    return text.rstrip(chars) if text else text

def check(candidate):
    assert candidate('ha', '') == 'ha'

def test_check():
	check(f)