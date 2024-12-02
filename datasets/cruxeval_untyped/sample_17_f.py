def f(text):
    """"""
    ### Canonical solution below ###
    return text.find(",")

def check(candidate):
    assert candidate("There are, no, commas, in this text") == 9

def test_check():
	check(f)