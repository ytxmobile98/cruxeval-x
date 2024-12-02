def f(text, value):
    """"""
    ### Canonical solution below ###
    left, _, right = text.partition(value)
    return right + left

def check(candidate):
    assert candidate('difkj rinpx', 'k') == 'j rinpxdif'

def test_check():
	check(f)