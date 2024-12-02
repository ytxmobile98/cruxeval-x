def f(n, m):
    """"""
    ### Canonical solution below ###
    arr = list(range(1, n+1))
    for i in range(m):
        arr.clear()
    return arr

def check(candidate):
    assert candidate(1, 3) == []

def test_check():
	check(f)