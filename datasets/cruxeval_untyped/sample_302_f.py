def f(string):
    """"""
    ### Canonical solution below ###
    return string.replace('needles', 'haystacks')

def check(candidate):
    assert candidate('wdeejjjzsjsjjsxjjneddaddddddefsfd') == 'wdeejjjzsjsjjsxjjneddaddddddefsfd'

def test_check():
	check(f)