def f(text):
    """"""
    ### Canonical solution below ###
    s = text.splitlines()
    return len(s)

def check(candidate):
    assert candidate("145\n\n12fjkjg") == 3

def test_check():
	check(f)