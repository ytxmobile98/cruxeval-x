def f(text, char, min_count):
    """"""
    ### Canonical solution below ###
    count = text.count(char)
    if count < min_count:
        return text.swapcase()
    return text

def check(candidate):
    assert candidate("wwwwhhhtttpp", 'w', 3) == 'wwwwhhhtttpp'

def test_check():
	check(f)