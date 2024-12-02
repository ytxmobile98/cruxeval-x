def f(names, excluded):
    """"""
    ### Canonical solution below ###
    excluded = excluded
    for i in range(len(names)):
        if excluded in names[i]:
            names[i] = names[i].replace(excluded, "")
    return names

def check(candidate):
    assert candidate(["avc  a .d e"], "") == ['avc  a .d e']

def test_check():
	check(f)