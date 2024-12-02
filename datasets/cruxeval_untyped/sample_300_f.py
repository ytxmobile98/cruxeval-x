def f(nums):
    """"""
    ### Canonical solution below ###
    count = 1
    for i in range(count, len(nums) - 1, 2):
        nums[i] = max(nums[i], nums[count-1])
        count += 1
    return nums

def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]

def test_check():
	check(f)