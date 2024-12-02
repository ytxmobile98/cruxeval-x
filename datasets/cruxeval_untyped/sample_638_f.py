def f(s, suffix):
    """"""
    ### Canonical solution below ###
    if not suffix:
        return s
    while s.endswith(suffix):
        s = s[:-len(suffix)]
    return s

def check(candidate):
    assert candidate('ababa', 'ab') == 'ababa'

def test_check():
	check(f)