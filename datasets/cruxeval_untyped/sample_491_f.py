def f(xs):
    """"""
    ### Canonical solution below ###
    for i in range(-1, -len(xs)-1, -1):
        xs.extend([xs[i], xs[i]])
    return xs

def check(candidate):
    assert candidate([4, 8, 8, 5]) == [4, 8, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5]

def test_check():
	check(f)