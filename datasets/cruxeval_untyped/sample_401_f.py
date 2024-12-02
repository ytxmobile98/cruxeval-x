def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if suffix and text.endswith(suffix):
        return text[:- len(suffix)]
    return text

def check(candidate):
    assert candidate('mathematics', 'example') == 'mathematics'

def test_check():
	check(f)