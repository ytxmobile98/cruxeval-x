def f(nums, sort_count):
    """"""
    ### Canonical solution below ###
    nums.sort()
    return nums[:sort_count]

def check(candidate):
    assert candidate([1, 2, 2, 3, 4, 5], 1) == [1]

def test_check():
	check(f)