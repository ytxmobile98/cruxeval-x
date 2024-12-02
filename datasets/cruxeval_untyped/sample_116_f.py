def f(d, count):
    """"""
    ### Canonical solution below ###
    for i in range(count):
        if d == {}:
            break
        d.popitem()
    return d

def check(candidate):
    assert candidate({}, 200) == {}

def test_check():
	check(f)