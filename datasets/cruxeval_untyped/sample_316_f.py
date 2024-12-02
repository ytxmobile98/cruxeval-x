def f(name):
    """"""
    ### Canonical solution below ###
    return '| ' + ' '.join(name.split(' ')) + ' |'

def check(candidate):
    assert candidate('i am your father') == '| i am your father |'

def test_check():
	check(f)