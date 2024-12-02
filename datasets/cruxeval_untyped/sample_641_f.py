def f(number):
    """"""
    ### Canonical solution below ###
    return True if number.isdecimal() else False

def check(candidate):
    assert candidate('dummy33;d') == False

def test_check():
	check(f)