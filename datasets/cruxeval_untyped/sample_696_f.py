def f(text):
    """"""
    ### Canonical solution below ###
    s = 0
    for i in range(1, len(text)):
        s += len(text.rpartition(text[i])[0])
    return s

def check(candidate):
    assert candidate('wdj') == 3

def test_check():
	check(f)