def f(text, char):
    """"""
    ### Canonical solution below ###
    if char in text:
        text = [t.strip() for t in text.split(char) if t]
        if len(text) > 1:
            return True
    return False

def check(candidate):
    assert candidate('only one line', ' ') == True

def test_check():
	check(f)