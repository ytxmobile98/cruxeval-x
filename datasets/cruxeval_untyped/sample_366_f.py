def f(string):
    """"""
    ### Canonical solution below ###
    tmp = string.lower()
    for char in string.lower():
        if char in tmp:
            tmp = tmp.replace(char, '', 1)
    return tmp

def check(candidate):
    assert candidate('[ Hello ]+ Hello, World!!_ Hi') == ''

def test_check():
	check(f)