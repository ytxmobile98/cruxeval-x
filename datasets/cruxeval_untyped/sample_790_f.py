def f(d):
    """"""
    ### Canonical solution below ###
    r = {
        'c': d.copy(),
        'd': d.copy()
    }
    return (r['c'] is r['d'], r['c'] == r['d'])

def check(candidate):
    assert candidate({'i': 1, 'love': 'parakeets'}) == (False, True)

def test_check():
	check(f)