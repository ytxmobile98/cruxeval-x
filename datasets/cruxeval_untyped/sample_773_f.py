def f(nums, n):
    """"""
    ### Canonical solution below ###
    return nums.pop(n)

def check(candidate):
    assert candidate([-7, 3, 1, -1, -1, 0, 4], 6) == 4

def test_check():
	check(f)