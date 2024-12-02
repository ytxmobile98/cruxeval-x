def f(base, k, v):
    """"""
    ### Canonical solution below ###
    base[k] = v
    return base

def check(candidate):
    assert candidate({37: 'forty-five'}, '23', 'what?') == {37: 'forty-five', '23': 'what?'}

def test_check():
	check(f)