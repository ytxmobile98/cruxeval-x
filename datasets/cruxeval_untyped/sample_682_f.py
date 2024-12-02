def f(text, length, index):
    """"""
    ### Canonical solution below ###
    ls = text.rsplit(None, index)
    return '_'.join([l[:length] for l in ls])

def check(candidate):
    assert candidate('hypernimovichyp', 2, 2) == 'hy'

def test_check():
	check(f)