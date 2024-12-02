def f(array, i_num, elem):
    """"""
    ### Canonical solution below ###
    array.insert(i_num, elem)
    return array

def check(candidate):
    assert candidate([ -4,   1,  0], 1, 4) == [-4, 4, 1, 0]

def test_check():
	check(f)