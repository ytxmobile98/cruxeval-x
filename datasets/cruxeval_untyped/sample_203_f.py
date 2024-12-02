def f(d):
    """"""
    ### Canonical solution below ###
    d.clear()
    return d

def check(candidate):
    assert candidate({'a': 3, 'b': -1, 'c': 'Dum'}) == {}

def test_check():
	check(f)