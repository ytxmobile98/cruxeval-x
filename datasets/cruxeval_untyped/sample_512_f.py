def f(s):
    """"""
    ### Canonical solution below ###
    return len(s) == s.count('0') + s.count('1')

def check(candidate):
    assert candidate('102') == False

def test_check():
	check(f)