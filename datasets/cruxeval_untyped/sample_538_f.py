def f(text, width):
    """"""
    ### Canonical solution below ###
    return text[:width].center(width, 'z')

def check(candidate):
    assert candidate('0574', 9) == 'zzz0574zz'

def test_check():
	check(f)