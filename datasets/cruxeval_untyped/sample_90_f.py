def f(array):
    """"""
    ### Canonical solution below ###
    return_arr = []
    for a in array:
        return_arr.append(a.copy())
    return return_arr

def check(candidate):
    assert candidate([[1, 2, 3], [], [1, 2, 3]]) == [[1, 2, 3], [], [1, 2, 3]]

def test_check():
	check(f)