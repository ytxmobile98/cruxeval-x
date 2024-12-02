def f(nums):
    """"""
    ### Canonical solution below ###
    copy = nums.copy()
    newDict = dict()
    for k in copy:
        newDict[k] = len(copy[k])
    return newDict

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)