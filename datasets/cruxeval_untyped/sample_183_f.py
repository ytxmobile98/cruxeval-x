def f(text):
    """"""
    ### Canonical solution below ###
    ls = text.split()
    lines = " ".join(ls[::3]).splitlines()
    res = []
    for i in range(2):
        ln = ls[1::3]
        if 3 * i + 1 < len(ln):
            res.append(" ".join(ln[3 * i:3 * (i + 1)]))
    return lines + res

def check(candidate):
    assert candidate("echo hello!!! nice!") == ['echo']

def test_check():
	check(f)