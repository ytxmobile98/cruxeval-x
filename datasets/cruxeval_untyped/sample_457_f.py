def f(nums):
    """"""
    ### Canonical solution below ###
    count = list(range(len(nums)))
    for i in range(len(nums)):
        nums.pop()
        if len(count) > 0:
            count.pop(0)
    return nums

def check(candidate):
    assert candidate([3, 1, 7, 5, 6]) == []

def test_check():
	check(f)