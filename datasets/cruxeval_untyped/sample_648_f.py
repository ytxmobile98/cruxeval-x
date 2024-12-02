def f(list1, list2):
    """"""
    ### Canonical solution below ###
    l = list1[:]
    while len(l) > 0:
        if l[-1] in list2:
            l.pop()
        else:
            return l[-1]
    return 'missing'

def check(candidate):
    assert candidate([0, 4, 5, 6], [13, 23, -5, 0]) == 6

def test_check():
	check(f)