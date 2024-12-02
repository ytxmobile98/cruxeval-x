def f(text, limit, char):
    """"""
    ### Canonical solution below ###
    if limit < len(text):
        return text[0:limit]
    return text.ljust(limit, char)

def check(candidate):
    assert candidate('tqzym', 5, 'c') == 'tqzym'

def test_check():
	check(f)