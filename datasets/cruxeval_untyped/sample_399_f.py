def f(text, old, new):
    """"""
    ### Canonical solution below ###
    if len(old) > 3:
        return text
    if old in text and ' ' not in text:
        return text.replace(old, new*len(old))
    while old in text:
        text = text.replace(old, new)
    return text

def check(candidate):
    assert candidate('avacado', 'va', '-') == 'a--cado'

def test_check():
	check(f)