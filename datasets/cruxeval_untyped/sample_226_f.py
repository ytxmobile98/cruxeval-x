def f(nums):
    """"""
    ### Canonical solution below ###
    for i in range(len(nums)):
        if nums[i] % 3 == 0:
            nums.append(nums[i])
    return nums

def check(candidate):
    assert candidate([1, 3]) == [1, 3, 3]

def test_check():
	check(f)