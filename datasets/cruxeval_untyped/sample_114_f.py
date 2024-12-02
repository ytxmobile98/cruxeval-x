def f(text, sep):
    """"""
    ### Canonical solution below ###
    return text.rsplit(sep, maxsplit=2)

def check(candidate):
    assert candidate("a-.-.b", "-.") == ['a', '', 'b']

def test_check():
	check(f)