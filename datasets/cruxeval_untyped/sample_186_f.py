def f(text):
    """"""
    ### Canonical solution below ###
    return ' '.join(map(str.lstrip, text.split()))

def check(candidate):
    assert candidate('pvtso') == 'pvtso'

def test_check():
	check(f)