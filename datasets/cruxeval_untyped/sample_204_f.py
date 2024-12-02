def f(name):
    """"""
    ### Canonical solution below ###
    return [name[0], name[1][::-1][0]]

def check(candidate):
    assert candidate("master. ") == ['m', 'a']

def test_check():
	check(f)