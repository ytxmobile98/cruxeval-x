def f(text, space_symbol, size):
    """"""
    ### Canonical solution below ###
    spaces = ''.join(space_symbol for i in range(size-len(text)))
    return text + spaces

def check(candidate):
    assert candidate('w', '))', 7) == 'w))))))))))))'

def test_check():
	check(f)