def f(nums):
    """"""
    ### Canonical solution below ###
    for _ in range(len(nums) - 1):
        nums.reverse()
    return nums

def check(candidate):
    assert candidate([1, -9, 7, 2, 6, -3, 3]) == [1, -9, 7, 2, 6, -3, 3]

def test_check():
	check(f)