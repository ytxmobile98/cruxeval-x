def f(d):
    """"""
    ### Canonical solution below ###
    keys = []
    for k in d:
        keys.append('%s => %s' % (k, d[k]))
    return keys

def check(candidate):
    assert candidate({'-4':'4','1':'2','-':'-3'}) == ['-4 => 4', '1 => 2', '- => -3']

def test_check():
	check(f)