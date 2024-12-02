def f(d):
    """"""
    ### Canonical solution below ###
    d['luck'] = 42
    d.clear()
    return {1: False, 2 :0}

def check(candidate):
    assert candidate({}) == {1: False, 2: 0}

def test_check():
	check(f)