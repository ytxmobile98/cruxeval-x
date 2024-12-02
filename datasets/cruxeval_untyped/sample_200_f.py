def f(text, value):
    """"""
    ### Canonical solution below ###
    length = len(text)
    index = 0
    while length > 0:
        value = text[index] + value
        length -= 1
        index += 1
    return value

def check(candidate):
    assert candidate('jao mt', 'house') == 'tm oajhouse'

def test_check():
	check(f)