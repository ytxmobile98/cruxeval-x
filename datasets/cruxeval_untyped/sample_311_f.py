def f(text):
    """"""
    ### Canonical solution below ###
    text = text.replace('#', '1').replace('$', '5')
    return 'yes' if text.isnumeric() else 'no'

def check(candidate):
    assert candidate('A') == 'no'

def test_check():
	check(f)