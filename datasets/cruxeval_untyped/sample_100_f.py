def f(d, rm):
    """"""
    ### Canonical solution below ###
    res = d.copy()
    for k in rm:
        if k in res:
            del res[k]
    return res

def check(candidate):
    assert candidate({'1': 'a', 1: 'a', 1: 'b', '1': 'b'}, [1]) == {'1': 'b'}

def test_check():
	check(f)