def f(t):
    """"""
    ### Canonical solution below ###
    a, sep, b = t.rpartition('-')
    if len(b) == len(a):
        return 'imbalanced'
    return a + b.replace(sep, '')

def check(candidate):
    assert candidate("fubarbaz") == 'fubarbaz'

def test_check():
	check(f)