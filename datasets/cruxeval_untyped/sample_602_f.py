def f(nums, target):
    """"""
    ### Canonical solution below ###
    cnt = nums.count(target)
    return cnt * 2

def check(candidate):
    assert candidate([1, 1], 1) == 4

def test_check():
	check(f)