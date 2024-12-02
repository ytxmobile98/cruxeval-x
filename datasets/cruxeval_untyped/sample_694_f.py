def f(d):
    """"""
    ### Canonical solution below ###
    i = len(d) - 1
    key = list(d.keys())[i]
    d.pop(key, None)
    return key, d

def check(candidate):
    assert candidate(dict(e=1, d=2, c=3)) == ('c', {'e': 1, 'd': 2})

def test_check():
	check(f)