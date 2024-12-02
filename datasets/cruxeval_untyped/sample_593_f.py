def f(nums, n):
    """"""
    ### Canonical solution below ###
    pos = len(nums) - 1
    for i in range(-len(nums), 0):
        nums.insert(pos, nums[i])
    return nums

def check(candidate):
    assert candidate([], 14) == []

def test_check():
	check(f)