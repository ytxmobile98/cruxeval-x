def f(text):
    """"""
    ### Canonical solution below ###
    nums = list(filter(str.isnumeric, text))
    assert len(nums) > 0
    return ''.join(nums)

def check(candidate):
    assert candidate('-123   \t+314') == '123314'

def test_check():
	check(f)