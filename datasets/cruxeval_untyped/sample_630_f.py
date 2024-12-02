def f(original, string):
    """"""
    ### Canonical solution below ###
    temp = dict(original)
    for a, b in string.items():
        temp[b] = a
    return temp

def check(candidate):
    assert candidate({1: -9, 0: -7}, {1: 2, 0: 3}) == {1: -9, 0: -7, 2: 1, 3: 0}

def test_check():
	check(f)