def f(text, char):
    """"""
    ### Canonical solution below ###
    return ' '.join(text.split(char, len(text)))

def check(candidate):
    assert candidate('a', 'a') == ' '

def test_check():
	check(f)