def f(l, c):
    """"""
    ### Canonical solution below ###
    return c.join(l)

def check(candidate):
    assert candidate(['many', 'letters', 'asvsz', 'hello', 'man'], '') == 'manylettersasvszhelloman'

def test_check():
	check(f)