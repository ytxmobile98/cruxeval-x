def f(nums):
    """"""
    ### Canonical solution below ###
    count = len(nums) // 2
    for _ in range(count):
        nums.pop(0)
    return nums

def check(candidate):
    assert candidate([3, 4, 1, 2, 3]) == [1, 2, 3]

def test_check():
	check(f)