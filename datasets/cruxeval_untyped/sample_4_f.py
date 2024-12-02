def f(array):
    """"""
    ### Canonical solution below ###
    s = ' '
    s += ''.join(array)
    return s

def check(candidate):
    assert candidate([' ', '  ', '    ', '   ']) == '           '

def test_check():
	check(f)