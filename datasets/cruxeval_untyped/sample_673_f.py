def f(string):
    """"""
    ### Canonical solution below ###
    if string.isupper():
        return string.lower()
    elif string.islower():
        return string.upper()
    return string

def check(candidate):
    assert candidate("cA") == 'cA'

def test_check():
	check(f)