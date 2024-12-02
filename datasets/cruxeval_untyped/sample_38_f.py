def f(string):
    """"""
    ### Canonical solution below ###
    return string.title().replace(' ', '')

def check(candidate):
    assert candidate('1oE-err bzz-bmm') == '1Oe-ErrBzz-Bmm'

def test_check():
	check(f)