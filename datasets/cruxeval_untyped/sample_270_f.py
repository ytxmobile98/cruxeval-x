def f(dic):
    """"""
    ### Canonical solution below ###
    d = {}
    for key in dic:
        d[key] = dic.popitem(last = False)[1]
    return d

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)