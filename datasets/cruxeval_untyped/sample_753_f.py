def f(bag):
    """"""
    ### Canonical solution below ###
    values = list(bag.values())
    tbl = {}
    for v in range(100):
        if v in values:
            tbl[v] = values.count(v)
    return tbl

def check(candidate):
    assert candidate({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}) == {0: 5}

def test_check():
	check(f)