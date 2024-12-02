def f(text, c):
    """"""
    ### Canonical solution below ###
    ls = list(text)
    if c not in text:
        raise ValueError('Text has no {c}')
    ls.pop(text.rindex(c))
    return ''.join(ls)

def check(candidate):
    assert candidate('uufhl', 'l') == 'uufh'

def test_check():
	check(f)