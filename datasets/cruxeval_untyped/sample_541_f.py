def f(text):
    """"""
    ### Canonical solution below ###
    return ''.join(list(text)).isspace()

def check(candidate):
    assert candidate(' \t  \u3000') == True

def test_check():
	check(f)