def f(text, delimiter):
    """"""
    ### Canonical solution below ###
    text = text.rpartition(delimiter)
    return text[0] + text[-1]

def check(candidate):
    assert candidate('xxjarczx', 'x') == 'xxjarcz'

def test_check():
	check(f)