def f(x, y):
    """"""
    ### Canonical solution below ###
    tmp = ''.join(['0' if c == '9' else '9' for c in y[::-1]])
    if (x.isnumeric() and tmp.isnumeric()):
        return x + tmp
    else:
        return x

def check(candidate):
    assert candidate("", "sdasdnakjsda80") == ''

def test_check():
	check(f)