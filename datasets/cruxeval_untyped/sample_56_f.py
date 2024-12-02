def f(sentence):
    """"""
    ### Canonical solution below ###
    for c in sentence:
        if c.isascii() is False:
            return False
        else:
            continue
    return True

def check(candidate):
    assert candidate('1z1z1') == True

def test_check():
	check(f)