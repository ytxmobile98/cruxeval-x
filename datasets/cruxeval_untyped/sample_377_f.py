def f(text):
    """"""
    ### Canonical solution below ###
    return ', '.join(text.splitlines())

def check(candidate):
    assert candidate("BYE\nNO\nWAY") == 'BYE, NO, WAY'

def test_check():
	check(f)