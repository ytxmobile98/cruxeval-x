def f(k, j):
    """"""
    ### Canonical solution below ###
    arr = []
    for i in range(k):
        arr.append(j)
    return arr

def check(candidate):
    assert candidate(7, 5) == [5, 5, 5, 5, 5, 5, 5]

def test_check():
	check(f)