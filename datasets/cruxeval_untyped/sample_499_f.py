def f(text, length, fillchar):
    """"""
    ### Canonical solution below ###
    size = len(text)
    return text.center(length, fillchar)

def check(candidate):
    assert candidate('magazine', 25, '.') == '.........magazine........'

def test_check():
	check(f)