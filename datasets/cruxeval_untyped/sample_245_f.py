def f(alphabet, s):
    """"""
    ### Canonical solution below ###
    a = [x for x in alphabet if x.upper() in s]
    if s.upper() == s:
        a.append('all_uppercased')
    return a

def check(candidate):
    assert candidate('abcdefghijklmnopqrstuvwxyz', "uppercased # % ^ @ ! vz.") == []

def test_check():
	check(f)