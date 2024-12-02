def f(text):
    """"""
    ### Canonical solution below ###
    for i in range(len(text)):
        if text[0:i].startswith("two"):
            return text[i:]
    return 'no'

def check(candidate):
    assert candidate("2two programmers") == 'no'

def test_check():
	check(f)