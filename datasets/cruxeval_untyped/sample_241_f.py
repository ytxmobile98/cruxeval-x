def f(postcode):
    """"""
    ### Canonical solution below ###
    return postcode[postcode.index('C'):]

def check(candidate):
    assert candidate('ED20 CW') == 'CW'

def test_check():
	check(f)