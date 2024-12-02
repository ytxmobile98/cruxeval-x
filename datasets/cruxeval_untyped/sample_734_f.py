def f(nums):
    """"""
    ### Canonical solution below ###
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] % 2 == 0:
            nums.remove(nums[i])
    return nums

def check(candidate):
    assert candidate([5, 3, 3, 7]) == [5, 3, 3, 7]

def test_check():
	check(f)