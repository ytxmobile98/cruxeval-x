def f(s):
    """"""
    ### Canonical solution below ###
    if str.isascii(s[-5:]):
        return s[-5:], s[0:][:3]
    elif str.isascii(s[:5]):
        return s[:5], s[-5:][3:]
    else:
        return s

def check(candidate):
    assert candidate('a1234år') == ('a1234', 'år')

def test_check():
	check(f)