def f(nums):
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        nums.insert(i, nums.pop(0))
    return nums

def check(candidate):
    assert candidate([0, -5, -4]) == [-4, -5, 0]

def test_check():
	check(f)