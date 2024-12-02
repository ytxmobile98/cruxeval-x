def f(dic):
    """"""
    ### Canonical solution below ###
    for k,v in sorted(dic.items(), key=lambda x: len(str(x)))[:-1]:
        dic.pop(k)
    return list(dic.items())

def check(candidate):
    assert candidate({'11': 52, '65': 34, 'a': 12, '4': 52, '74': 31}) == [('74', 31)]

def test_check():
	check(f)