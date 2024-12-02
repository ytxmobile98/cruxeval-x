def f(text):
    """"""
    ### Canonical solution below ###
    result = []
    for i, ch in enumerate(text):
        if ch == ch.lower():
            continue
        if len(text) - 1 - i < text.rindex(ch.lower()):
            result.append(ch)
    return ''.join(result)

def check(candidate):
    assert candidate('ru') == ''

def test_check():
	check(f)