def f(nums):
    """"""
    ### Canonical solution below ###
    for odd in nums[:]:
        if odd % 2 != 0:
            nums.remove(odd)
    sum_ = 0
    for num in nums:
        sum_ += num
    return sum_

def check(candidate):
    assert candidate([11, 21, 0, 11]) == 0

def test_check():
	check(f)