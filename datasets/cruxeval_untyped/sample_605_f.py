def f(nums):
    """"""
    ### Canonical solution below ###
    nums.clear()
    return "quack"

def check(candidate):
    assert candidate([2, 5, 1, 7, 9, 3]) == 'quack'

def test_check():
	check(f)