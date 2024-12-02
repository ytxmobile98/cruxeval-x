def f(str, n):
    """"""
    ### Canonical solution below ###
    if len(str) < n:
        return str
    else:
        return str.removeprefix(str[:n])

def check(candidate):
    assert candidate("try.", 5) == 'try.'

def test_check():
	check(f)