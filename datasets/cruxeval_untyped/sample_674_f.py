def f(text):
    """"""
    ### Canonical solution below ###
    ls = list(text)
    for x in range(len(ls)-1, -1, -1):
        if len(ls) <= 1: break
        if ls[x] not in 'zyxwvutsrqponmlkjihgfedcba': ls.pop(ls[x])
    return ''.join(ls)

def check(candidate):
    assert candidate('qq') == 'qq'

def test_check():
	check(f)