def f(text, fill, size):
    """"""
    ### Canonical solution below ###
    if size < 0:
        size = -size
    if len(text) > size:
        return text[len(text) - size:]
    return text.rjust(size, fill)

def check(candidate):
    assert candidate('no asw', 'j', 1) == 'w'

def test_check():
	check(f)