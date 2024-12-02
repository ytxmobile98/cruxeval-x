def f(text):
    """"""
    ### Canonical solution below ###
    return text.split(':')[0].count('#')

def check(candidate):
    assert candidate("#! : #!") == 1

def test_check():
	check(f)