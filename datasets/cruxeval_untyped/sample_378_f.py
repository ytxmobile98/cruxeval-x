def f(dic, key):
    """"""
    ### Canonical solution below ###
    dic = dict(dic)
    v = dic.pop(key, 0)
    if v == 0:
        return 'No such key!'
    while len(dic) > 0:
        dic[dic.popitem()[1]] = dic.popitem()[0]
    return int(dic.popitem()[0])

def check(candidate):
    assert candidate(dict(did=0), 'u') == 'No such key!'

def test_check():
	check(f)