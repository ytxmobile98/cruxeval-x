def f(s):
    """"""
    ### Canonical solution below ###
    return '{}{}{}'.format(s[3:], s[2], s[5:8])

def check(candidate):
    assert candidate('jbucwc') == 'cwcuc'

def test_check():
	check(f)