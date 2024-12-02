def f(n):
    """"""
    ### Canonical solution below ###
    for i in str(n):
        if not i.isdigit():
            n = -1
            break
    return n

def check(candidate):
    assert candidate("6 ** 2") == -1

def test_check():
	check(f)