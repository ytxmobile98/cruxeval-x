def f(nums):
    """"""
    ### Canonical solution below ###
    for i in range(len(nums)-1, -1, -1):
        if nums[i] % 2 == 1:
            nums.insert(i+1, nums[i])
    return nums

def check(candidate):
    assert candidate([2, 3, 4, 6, -2]) == [2, 3, 3, 4, 6, -2]

def test_check():
	check(f)