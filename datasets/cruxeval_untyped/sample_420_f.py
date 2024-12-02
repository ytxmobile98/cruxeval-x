def f(text):
    """"""
    ### Canonical solution below ###
    try:
        return text.isalpha()
    except:
        return False

def check(candidate):
    assert candidate("x") == True

def test_check():
	check(f)