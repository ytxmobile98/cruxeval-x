def f(r, w):
    """"""
    ### Canonical solution below ###
    a = []
    if r[0] == w[0] and w[-1] == r[-1]:
        a.append(r)
        a.append(w)
    else:
        a.append(w)
        a.append(r)
    return a

def check(candidate):
    assert candidate("ab", "xy") == ['xy', 'ab']

def test_check():
	check(f)