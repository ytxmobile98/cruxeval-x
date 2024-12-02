def f(l1, l2):
    """"""
    ### Canonical solution below ###
    if len(l1) != len(l2):
        return {}
    return dict.fromkeys(l1, l2)

def check(candidate):
    assert candidate(['a', 'b'], ['car', 'dog']) == {'a': ['car', 'dog'], 'b': ['car', 'dog']}

def test_check():
	check(f)