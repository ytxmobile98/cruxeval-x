def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

def check(candidate):
    assert candidate('zejrohaj', 'owc') == 'zejrohaj'

def test_check():
	check(f)