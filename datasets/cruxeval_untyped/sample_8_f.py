def f(string, encryption):
    """"""
    ### Canonical solution below ###
    if encryption == 0:
        return string
    else:
        return string.upper().encode('rot13')

def check(candidate):
    assert candidate('UppEr', 0) == 'UppEr'

def test_check():
	check(f)