def f(text1, text2):
    """"""
    ### Canonical solution below ###
    nums = []
    for i in range(len(text2)):
        nums.append(text1.count(text2[i]))
    return sum(nums)

def check(candidate):
    assert candidate('jivespdcxc', 'sx') == 2

def test_check():
	check(f)