def f(name):
    """"""
    ### Canonical solution below ###
    return '*'.join(name.split(' '))

def check(candidate):
    assert candidate('Fred Smith') == 'Fred*Smith'

def test_check():
	check(f)