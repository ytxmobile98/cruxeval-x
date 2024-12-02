def f(s):
    """"""
    ### Canonical solution below ###
    return ''.join([c for c in s if c.isspace()])

def check(candidate):
    assert candidate( '\ngiyixjkvu\n\r\r \frgjuo') == '\n\n\r\r \x0c'

def test_check():
	check(f)