def f(nums, pop1, pop2):
    """"""
    ### Canonical solution below ###
    nums.pop(pop1 - 1)
    nums.pop(pop2 - 1)
    return nums

def check(candidate):
    assert candidate([1, 5, 2, 3, 6], 2, 4) == [1, 2, 3]

def test_check():
	check(f)