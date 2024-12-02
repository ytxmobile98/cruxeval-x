def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if suffix == '':
        suffix = None
    return text.endswith(suffix)

def check(candidate):
    assert candidate('uMeGndkGh', 'kG') == False

def test_check():
	check(f)