def f(text):
    """"""
    ### Canonical solution below ###
    return not text.isdecimal()

def check(candidate):
    assert candidate('the speed is -36 miles per hour') == True

def test_check():
	check(f)