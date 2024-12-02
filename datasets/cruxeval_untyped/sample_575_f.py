def f(nums, val):
    """"""
    ### Canonical solution below ###
    new_list = []
    [new_list.extend([i] * val) for i in nums]
    return sum(new_list)

def check(candidate):
    assert candidate([10, 4], 3) == 42

def test_check():
	check(f)