def f(a):
    """"""
    ### Canonical solution below ###
    b = a.copy()
    for k in range(0, len(a) - 1, 2):
        b.insert(k + 1, b[k])
    b.append(b[0])
    return b

def check(candidate):
    assert candidate([5, 5, 5, 6, 4, 9]) == [5, 5, 5, 5, 5, 5, 6, 4, 9, 5]

def test_check():
	check(f)