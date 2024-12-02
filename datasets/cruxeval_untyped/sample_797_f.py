def f(dct):
    """"""
    ### Canonical solution below ###
    lst = []
    for key in sorted(dct):
        lst.append((key, dct[key]))
    return lst

def check(candidate):
    assert candidate({'a': 1, 'b': 2, 'c': 3}) == [('a', 1), ('b', 2), ('c', 3)]

def test_check():
	check(f)