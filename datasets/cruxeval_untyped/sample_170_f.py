def f(nums, number):
    """"""
    ### Canonical solution below ###
    return nums.count(number)

def check(candidate):
    assert candidate([12, 0, 13, 4, 12], 12) == 2

def test_check():
	check(f)