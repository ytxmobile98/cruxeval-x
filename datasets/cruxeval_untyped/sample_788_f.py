def f(text, suffix):
    """"""
    ### Canonical solution below ###
    if suffix.startswith("/"):
        return text + suffix[1:]
    return text

def check(candidate):
    assert candidate('hello.txt', '/') == 'hello.txt'

def test_check():
	check(f)