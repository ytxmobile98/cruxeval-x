def f(s):
    """"""
    ### Canonical solution below ###
    l = list(s)
    for i in range(len(l)):
        l[i] = l[i].lower()
        if not l[i].isdigit():
            return False
    return True

def check(candidate):
    assert candidate("") == True

def test_check():
	check(f)