def f(text):
    """"""
    ### Canonical solution below ###
    if text.islower():
        return True
    return False

def check(candidate):
    assert candidate("54882") == False

def test_check():
	check(f)