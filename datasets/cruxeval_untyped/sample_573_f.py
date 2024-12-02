def f(string, prefix):
    """"""
    ### Canonical solution below ###
    if string.startswith(prefix):
        return string.removeprefix(prefix)
    return string

def check(candidate):
    assert candidate("Vipra", "via") == 'Vipra'

def test_check():
	check(f)