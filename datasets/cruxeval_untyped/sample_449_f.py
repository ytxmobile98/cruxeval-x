def f(x):
    """"""
    ### Canonical solution below ###
    n = len(x)
    i = 0
    while i < n and x[i].isdigit():
        i += 1
    return i == n

def check(candidate):
    assert candidate('1') == True

def test_check():
	check(f)