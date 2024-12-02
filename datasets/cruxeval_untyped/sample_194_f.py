def f(matr, insert_loc):
    """"""
    ### Canonical solution below ###
    matr.insert(insert_loc, [])
    return matr

def check(candidate):
    assert candidate([[5, 6, 2, 3], [1, 9, 5, 6]], 0) == [[], [5, 6, 2, 3], [1, 9, 5, 6]]

def test_check():
	check(f)