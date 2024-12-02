def f(s):
    """"""
    ### Canonical solution below ###
    return s.replace('(', '[').replace(')', ']')

def check(candidate):
    assert candidate("(ac)") == '[ac]'

def test_check():
	check(f)