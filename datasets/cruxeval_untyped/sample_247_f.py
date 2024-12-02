def f(s):
    """"""
    ### Canonical solution below ###
    if s.isalpha():
        return "yes"
    if s == "":
        return "str is empty"
    return "no"

def check(candidate):
    assert candidate('Boolean') == 'yes'

def test_check():
	check(f)