def f(d):
    """"""
    ### Canonical solution below ###
    d = d.copy()
    d.popitem()
    return d

def check(candidate):
    assert candidate({"l": 1, "t": 2, "x:": 3}) == {'l': 1, 't': 2}

def test_check():
	check(f)