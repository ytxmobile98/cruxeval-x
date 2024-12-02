def f(d):
    """"""
    ### Canonical solution below ###
    return dict(d.items())

def check(candidate):
    assert candidate({'a': 42, 'b': 1337, 'c': -1, 'd': 5}) == {'a': 42, 'b': 1337, 'c': -1, 'd': 5}

def test_check():
	check(f)