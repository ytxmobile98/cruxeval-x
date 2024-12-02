def f(d):
    """"""
    ### Canonical solution below ###
    i = iter(d.items())
    return next(i), next(i)

def check(candidate):
    assert candidate({'a': 123, 'b': 456, 'c': 789}) == (('a', 123), ('b', 456))

def test_check():
	check(f)