def f(array, elem):
    """"""
    ### Canonical solution below ###
    k = 0
    l = array.copy()
    for i in l:
        if i > elem:
            array.insert(k, elem)
            break
        k += 1
    return array

def check(candidate):
    assert candidate([5, 4, 3, 2, 1, 0], 3) == [3, 5, 4, 3, 2, 1, 0]

def test_check():
	check(f)