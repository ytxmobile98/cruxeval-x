def f(base_list, nums):
    """"""
    ### Canonical solution below ###
    base_list.extend(nums)
    res = base_list.copy()
    for i in range(-len(nums), 0):
        res.append(res[i])
    return res

def check(candidate):
    assert candidate([9, 7, 5, 3, 1], [2, 4, 6, 8, 0]) == [9, 7, 5, 3, 1, 2, 4, 6, 8, 0, 2, 6, 0, 6, 6]

def test_check():
	check(f)