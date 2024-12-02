def f(nums, i):
    """"""
    ### Canonical solution below ###
    nums.pop(i)
    return nums

def check(candidate):
    assert candidate([35, 45, 3, 61, 39, 27, 47], 0) == [45, 3, 61, 39, 27, 47]

def test_check():
	check(f)