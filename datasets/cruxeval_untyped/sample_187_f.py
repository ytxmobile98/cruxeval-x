def f(d, index):
    """"""
    ### Canonical solution below ###
    length = len(d.items())
    idx = index % length
    v = d.popitem()[1]
    for _ in range(idx):
        d.popitem()
    return v

def check(candidate):
    assert candidate({27:39}, 1) == 39

def test_check():
	check(f)