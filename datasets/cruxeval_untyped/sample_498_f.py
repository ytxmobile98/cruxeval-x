def f(nums, idx, added):
    """"""
    ### Canonical solution below ###
    nums[idx:idx] = (added,)
    return nums

def check(candidate):
    assert candidate([2, 2, 2, 3, 3], 2, 3) == [2, 2, 3, 2, 3, 3]

def test_check():
	check(f)