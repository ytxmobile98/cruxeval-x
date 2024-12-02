def f(arr1, arr2):
    """"""
    ### Canonical solution below ###
    new_arr = arr1.copy()
    new_arr.extend(arr2)
    return new_arr

def check(candidate):
    assert candidate([5, 1, 3, 7, 8], ['', 0, -1, []]) == [5, 1, 3, 7, 8, '', 0, -1, []]

def test_check():
	check(f)