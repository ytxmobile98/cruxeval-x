def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if text.endswith(suffix):
        text = text[:-1] + text[-1:].swapcase()
    return text

def check(candidate):
    assert candidate('damdrodm', 'm') == 'damdrodM'

def test_check():
	check(f)