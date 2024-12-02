def f(dic, inx):
    """"""
    ### Canonical solution below ###
    try:
        dic[list(dic)[list(dic).index(inx)]] = list(dic)[list(dic).index(inx)].lower()
    except ValueError:
        pass
    return list(dic.items())

def check(candidate):
    assert candidate({"Bulls": 23, "White Sox": 45}, "Bulls") == [('Bulls', 'bulls'), ('White Sox', 45)]

def test_check():
	check(f)