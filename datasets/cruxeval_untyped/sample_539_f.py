def f(array):
    """"""
    ### Canonical solution below ###
    c = array
    array_copy = array

    while True:
        c.append('_')
        if c == array_copy:
            array_copy[c.index('_')] = ''
            break
        
    return array_copy

def check(candidate):
    assert candidate([]) == ['']

def test_check():
	check(f)