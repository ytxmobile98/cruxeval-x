def f(text):
    """"""
    ### Canonical solution below ###
    b = True
    for x in text:
        if x.isdigit():
            b = True
        else:
            b = False
            break
    return b

def check(candidate):
    assert candidate("-1-3") == False

def test_check():
	check(f)