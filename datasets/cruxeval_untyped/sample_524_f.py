def f(dict0):
    """"""
    ### Canonical solution below ###
    new = dict0.copy()
    for i in range(len(new)-1):
        dict0[sorted(new)[i]] = i
    return dict0

def check(candidate):
    assert candidate({2: 5, 4: 1, 3: 5, 1: 3, 5: 1}) == {2: 1, 4: 3, 3: 2, 1: 0, 5: 1}

def test_check():
	check(f)