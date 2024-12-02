def f(text, splitter):
    """"""
    ### Canonical solution below ###
    return splitter.join(text.lower().split())

def check(candidate):
    assert candidate('LlTHH sAfLAPkPhtsWP', '#') == 'llthh#saflapkphtswp'

def test_check():
	check(f)