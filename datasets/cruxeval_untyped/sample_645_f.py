def f(nums, target):
    """"""
    ### Canonical solution below ###
    if nums.count(0):
        return 0
    elif nums.count(target) < 3:
        return 1
    else:
        return nums.index(target)

def check(candidate):
    assert candidate([1, 1, 1, 2], 3) == 1

def test_check():
	check(f)