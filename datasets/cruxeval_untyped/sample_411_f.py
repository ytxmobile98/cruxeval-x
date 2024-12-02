def f(text, pref):
    """"""
    ### Canonical solution below ###
    if isinstance(pref, list):
        return ', '.join(text.startswith(x) for x in pref)
    else:
        return text.startswith(pref)

def check(candidate):
    assert candidate('Hello World', 'W') == False

def test_check():
	check(f)