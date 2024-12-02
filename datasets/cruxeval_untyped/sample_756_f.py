def f(text):
    """"""
    ### Canonical solution below ###
    if text.isalnum() and all(i.isdigit() for i in text):
        return 'integer'
    return 'string'

def check(candidate):
    assert candidate('') == 'string'

def test_check():
	check(f)