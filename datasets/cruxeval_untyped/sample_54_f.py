def f(text, s, e):
    """"""
    ### Canonical solution below ###
    sublist = text[s:e]
    if not sublist:
        return -1
    return sublist.index(min(sublist))

def check(candidate):
    assert candidate('happy', 0, 3) == 1

def test_check():
	check(f)