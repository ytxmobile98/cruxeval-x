def f(items, target):
    """"""
    ### Canonical solution below ###
    if target in items:
        return items.index(target)
    return -1

def check(candidate):
    assert candidate(['''1''', '+', '-', '**', '//', '*', '+'], '**') == 3

def test_check():
	check(f)