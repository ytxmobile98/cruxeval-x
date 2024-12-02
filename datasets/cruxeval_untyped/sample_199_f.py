def f(str, char):
    """"""
    ### Canonical solution below ###
    base = char * (str.count(char) + 1)
    return str.removesuffix(base)

def check(candidate):
    assert candidate('mnmnj krupa...##!@#!@#$$@##', '@') == 'mnmnj krupa...##!@#!@#$$@##'

def test_check():
	check(f)