def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if suffix and text and text.endswith(suffix):
        return text.removesuffix(suffix)
    else:
        return text

def check(candidate):
    assert candidate('spider', 'ed') == 'spider'

def test_check():
	check(f)