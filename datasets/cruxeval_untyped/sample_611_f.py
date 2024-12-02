def f(nums):
    """"""
    ### Canonical solution below ###
    nums[:] = nums[::-1]
    return nums

def check(candidate):
    assert candidate([-6, -2, 1, -3, 0, 1]) == [1, 0, -3, 1, -2, -6]

def test_check():
	check(f)