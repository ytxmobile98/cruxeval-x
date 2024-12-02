def f(nums):
    """"""
    ### Canonical solution below ###
    nums.reverse()
    return ''.join(map(str, nums))

def check(candidate):
    assert candidate([-1, 9, 3, 1, -2]) == '-2139-1'

def test_check():
	check(f)