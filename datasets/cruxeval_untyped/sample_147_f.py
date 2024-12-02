def f(nums):
    """"""
    ### Canonical solution below ###
    middle = len(nums)//2
    return nums[middle:] + nums[0:middle]

def check(candidate):
    assert candidate([1, 1, 1]) == [1, 1, 1]

def test_check():
	check(f)