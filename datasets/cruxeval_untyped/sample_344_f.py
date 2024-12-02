def f(list, operation):
    """"""
    ### Canonical solution below ###
    new_list = list[:]
    new_list.sort()
    operation(new_list)
    return list

def check(candidate):
    assert candidate([6, 4, 2, 8, 15], (lambda x: x.reverse())) == [6, 4, 2, 8, 15]

def test_check():
	check(f)