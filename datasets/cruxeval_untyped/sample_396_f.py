def f(ets):
    """"""
    ### Canonical solution below ###
    while ets:
        k, v = ets.popitem()
        ets[k] = v**2
    return ets

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)