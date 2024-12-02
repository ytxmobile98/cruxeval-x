def f(nums, mos):
    """"""
    ### Canonical solution below ###
    for num in mos:
        nums.pop(nums.index(num))
    nums.sort()
    for num in mos:
        nums += [num]
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def check(candidate):
    assert candidate([3, 1, 2, 1, 4, 1], [1]) == False

def test_check():
	check(f)