def f(text):
    """"""
    ### Canonical solution below ###
    return text.count('-') == len(text)

def check(candidate):
    assert candidate("---123-4") == False

def test_check():
	check(f)