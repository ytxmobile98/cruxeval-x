def f(chars):
    """"""
    ### Canonical solution below ###
    s = ""
    for ch in chars:
        if chars.count(ch) % 2 == 0:
            s += ch.upper()
        else:
            s += ch
    return s

def check(candidate):
    assert candidate("acbced") == 'aCbCed'

def test_check():
	check(f)