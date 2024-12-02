def f(text, pref):
    """"""
    ### Canonical solution below ###
    if text.startswith(pref):
        n = len(pref)
        text = '.'.join(text[n:].split('.')[1:] + text[:n].split('.')[:-1])
    return text

def check(candidate):
    assert candidate('omeunhwpvr.dq', 'omeunh') == 'dq'

def test_check():
	check(f)