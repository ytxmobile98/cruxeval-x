def f(text, start):
    """"""
    ### Canonical solution below ###
    return text.startswith(start)

def check(candidate):
    assert candidate("Hello world", "Hello") == True

def test_check():
	check(f)