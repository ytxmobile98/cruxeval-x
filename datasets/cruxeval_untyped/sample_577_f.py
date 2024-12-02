def f(items):
    """"""
    ### Canonical solution below ###
    result = []
    for number in items:
        d = dict(items).copy()
        d.popitem()
        result.append(d)
        items = d
    return result

def check(candidate):
    assert candidate([(1, 'pos')]) == [{}]

def test_check():
	check(f)