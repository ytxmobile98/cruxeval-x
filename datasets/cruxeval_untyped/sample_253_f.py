def f(text, pref):
    """"""
    ### Canonical solution below ###
    length = len(pref)
    if pref == text[:length]:
        return text[length:]
    return text

def check(candidate):
    assert candidate('kumwwfv', 'k') == 'umwwfv'

def test_check():
	check(f)