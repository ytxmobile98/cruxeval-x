def f(text, char):
    """"""
    ### Canonical solution below ###
    text = list(text)
    for count, item in enumerate(text):
        if item == char:
            text.remove(item)
            return ''.join(text)
    return text

def check(candidate):
    assert candidate('pn', 'p') == 'n'

def test_check():
	check(f)