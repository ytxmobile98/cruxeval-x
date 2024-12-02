def f(nums, verdict):
    """"""
    ### Canonical solution below ###
    res = [x for x in nums if x != 0]
    result = [[x, verdict(x)] for x in res]
    if result:
        return result
    return 'error - no numbers or all zeros!'

def check(candidate):
    assert candidate([0, 3, 0, 1], lambda x: x < 2) == [[3, False], [1, True]]

def test_check():
	check(f)