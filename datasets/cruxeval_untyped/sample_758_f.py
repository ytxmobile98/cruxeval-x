def f(nums):
    """"""
    ### Canonical solution below ###
    if nums[::-1] == nums:
        return True
    return False

def check(candidate):
    assert candidate([0, 3, 6, 2]) == False

def test_check():
	check(f)