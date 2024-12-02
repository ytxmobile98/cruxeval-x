def f(nums, delete):
    """"""
    ### Canonical solution below ###
    nums.remove(delete)
    return nums

def check(candidate):
    assert candidate([4, 5, 3, 6, 1], 5) == [4, 3, 6, 1]

def test_check():
	check(f)