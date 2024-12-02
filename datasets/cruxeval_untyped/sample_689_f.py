def f(arr):
    """"""
    ### Canonical solution below ###
    count = len(arr)
    sub = arr.copy()
    for i in range(0, count, 2):
        sub[i] *= 5
    return sub

def check(candidate):
    assert candidate([-3, -6, 2, 7]) == [-15, -6, 10, 7]

def test_check():
	check(f)