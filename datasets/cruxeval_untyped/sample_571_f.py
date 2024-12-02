def f(input_string, spaces):
    """"""
    ### Canonical solution below ###
    return input_string.expandtabs(spaces)

def check(candidate):
    assert candidate(r'a\tb', 4) == 'a\\tb'

def test_check():
	check(f)