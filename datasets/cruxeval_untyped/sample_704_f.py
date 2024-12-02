def f(s, n, c):
    """"""
    ### Canonical solution below ###
    width = len(c)*n
    for _ in range(width - len(s)):
        s = c + s
    return s

def check(candidate):
    assert candidate('.', 0, '99') == '.'

def test_check():
	check(f)