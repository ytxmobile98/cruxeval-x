def f(text, char):
    """"""
    ### Canonical solution below ###
    position = len(text)
    if char in text:
        position = text.index(char)
        if position > 1:
            position = (position + 1) % len(text)
    return position

def check(candidate):
    assert candidate('wduhzxlfk', 'w') == 0

def test_check():
	check(f)