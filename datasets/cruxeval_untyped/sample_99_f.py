def f(text, sep, num):
    """"""
    ### Canonical solution below ###
    return '___'.join(text.rsplit(sep, num))

def check(candidate):
    assert candidate('aa+++bb', '+', 1) == 'aa++___bb'

def test_check():
	check(f)