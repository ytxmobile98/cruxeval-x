def f(text, tab_size):
    """"""
    ### Canonical solution below ###
    return text.replace('\t', ' '*tab_size)

def check(candidate):
    assert candidate('a', 100) == 'a'

def test_check():
	check(f)