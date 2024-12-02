def f(text):
    """"""
    ### Canonical solution below ###
    if not text.istitle():
        return text.title()
    return text.lower()

def check(candidate):
    assert candidate("PermissioN is GRANTed") == 'Permission Is Granted'

def test_check():
	check(f)