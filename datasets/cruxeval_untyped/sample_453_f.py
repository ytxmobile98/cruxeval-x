def f(string, c):
    """"""
    ### Canonical solution below ###
    return string.endswith(c)

def check(candidate):
    assert candidate('wrsch)xjmb8', 'c') == False

def test_check():
	check(f)