def f(a, b):
    """"""
    ### Canonical solution below ###
    d = dict(zip(a, b))
    a.sort(key=d.get, reverse=True)
    return [d.pop(x) for x in a]

def check(candidate):
    assert candidate(['12','ab'], [2,2]) == [2, 2]

def test_check():
	check(f)