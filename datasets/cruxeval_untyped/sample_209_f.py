def f(prefix, s):
    """"""
    ### Canonical solution below ###
    return str.removeprefix(prefix, s)

def check(candidate):
    assert candidate('hymi', 'hymifulhxhzpnyihyf') == 'hymi'

def test_check():
	check(f)