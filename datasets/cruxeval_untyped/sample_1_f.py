def f(a, b, c):
    """"""
    ### Canonical solution below ###
    result = {}
    for d in a, b, c:
        result.update(dict.fromkeys(d))
    return result

def check(candidate):
    assert candidate((1, ), (1, ), (1, 2)) == {1: None, 2: None}

def test_check():
	check(f)