def f(text):
    """"""
    ### Canonical solution below ###
    counter = 0
    for char in text:
        if char.isalpha():
            counter += 1
    return counter

def check(candidate):
    assert candidate('l000*',) == 1

def test_check():
	check(f)