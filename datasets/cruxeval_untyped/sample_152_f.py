def f(text):
    """"""
    ### Canonical solution below ###
    n = 0
    for char in text:
        if char.isupper():
            n += 1
    return n

def check(candidate):
    assert candidate(''.join(['A'] * 20)) == 20

def test_check():
	check(f)