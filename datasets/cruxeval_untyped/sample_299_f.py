def f(text, char):
    """"""
    ### Canonical solution below ###
    if not text.endswith(char):
        return f(char + text, char)
    return text

def check(candidate):
    assert candidate('staovk', 'k') == 'staovk'

def test_check():
	check(f)