def f(text, value):
    """"""
    ### Canonical solution below ###
    if not value in text:
        return ''
    return text.rpartition(value)[0]

def check(candidate):
    assert candidate('mmfbifen', 'i') == 'mmfb'

def test_check():
	check(f)