def f(array, elem):
    """"""
    ### Canonical solution below ###
    for idx, e in enumerate(array):
        if e > elem and array[idx - 1] < elem:
            array.insert(idx, elem)
    return array

def check(candidate):
    assert candidate([1, 2, 3, 5, 8], 6) == [1, 2, 3, 5, 6, 8]

def test_check():
	check(f)