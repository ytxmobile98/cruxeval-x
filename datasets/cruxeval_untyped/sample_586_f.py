def f(text, char):
    """"""
    ### Canonical solution below ###
    return text.rindex(char)

def check(candidate):
    assert candidate("breakfast", "e") == 2

def test_check():
	check(f)