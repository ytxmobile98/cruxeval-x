def f(prefix, text):
    """"""
    ### Canonical solution below ###
    if text.startswith(prefix):
        return text
    else:
        return prefix + text

def check(candidate):
    assert candidate('mjs', 'mjqwmjsqjwisojqwiso') == 'mjsmjqwmjsqjwisojqwiso'

def test_check():
	check(f)