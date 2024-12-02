def f(text):
    """"""
    ### Canonical solution below ###
    if not text.strip():
        return len(text.strip())
    return None

def check(candidate):
    assert candidate(" \t ") == 0

def test_check():
	check(f)