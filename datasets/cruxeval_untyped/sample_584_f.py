def f(txt):
    """"""
    ### Canonical solution below ###
    return txt.format(*('0'*20,))

def check(candidate):
    assert candidate("5123807309875480094949830") == '5123807309875480094949830'

def test_check():
	check(f)