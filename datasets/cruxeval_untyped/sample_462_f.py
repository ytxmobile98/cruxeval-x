def f(text, value):
    """"""
    ### Canonical solution below ###
    length = len(text)
    letters = list(text)
    if value not in letters:
        value = letters[0]
    return value * length

def check(candidate):
    assert candidate('ldebgp o', 'o') == 'oooooooo'

def test_check():
	check(f)