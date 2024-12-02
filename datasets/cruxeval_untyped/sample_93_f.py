def f(n):
    """"""
    ### Canonical solution below ###
    length = len(n) + 2
    revn = list(n)
    result = ''.join(revn)
    revn.clear()
    return result + ('!' * length)

def check(candidate):
    assert candidate('iq') == 'iq!!!!'

def test_check():
	check(f)