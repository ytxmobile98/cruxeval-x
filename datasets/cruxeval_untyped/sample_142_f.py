def f(x):
    """"""
    ### Canonical solution below ###
    if x.islower():
        return x
    else:
        return x[::-1]

def check(candidate):
    assert candidate('ykdfhp') == 'ykdfhp'

def test_check():
	check(f)