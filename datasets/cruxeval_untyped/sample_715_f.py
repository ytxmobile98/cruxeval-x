def f(text, char):
    """"""
    ### Canonical solution below ###
    return text.count(char) % 2 != 0

def check(candidate):
    assert candidate('abababac', 'a') == False

def test_check():
	check(f)