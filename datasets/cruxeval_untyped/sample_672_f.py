def f(text, position, value):
    """"""
    ### Canonical solution below ###
    length = len(text)
    index = (position % (length + 2)) - 1
    if index >= length or index < 0:
        return text
    text[index] = value
    return ''.join(text)

def check(candidate):
    assert candidate("1zd", 0, 'm') == '1zd'

def test_check():
	check(f)