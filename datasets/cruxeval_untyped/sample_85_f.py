def f(n):
    """"""
    ### Canonical solution below ###
    values = {0: 3, 1: 4.5, 2: '-'}
    res = {}
    for i, j in values.items():
        if i % n != 2:
            res[j] = n // 2
    return sorted(res)

def check(candidate):
    assert candidate(12) == [3, 4.5]

def test_check():
	check(f)