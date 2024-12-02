def f(nums, pos, value):
    """"""
    ### Canonical solution below ###
    nums.insert(pos, value)
    return nums

def check(candidate):
    assert candidate([3, 1, 2], 2, 0) == [3, 1, 0, 2]

def test_check():
	check(f)