def f(total, arg):
    """"""
    ### Canonical solution below ###
    if type(arg) is list:
        for e in arg:
            total.extend(e)
    else:
        total.extend(arg)
    return total

def check(candidate):
    assert candidate([1, 2, 3], 'nammo') == [1, 2, 3, 'n', 'a', 'm', 'm', 'o']

def test_check():
	check(f)