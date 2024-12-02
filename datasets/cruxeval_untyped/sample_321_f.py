def f(update, starting):
    """"""
    ### Canonical solution below ###
    d = starting.copy()
    for k in update:
        if k in d:
            d[k] += update[k]
        else:
            d[k] = update[k]
    return d

def check(candidate):
    assert candidate({}, {'desciduous': 2}) == {'desciduous': 2}

def test_check():
	check(f)