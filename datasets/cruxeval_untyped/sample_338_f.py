def f(my_dict):
    """"""
    ### Canonical solution below ###
    result = {v: k for k, v in my_dict.items()}
    return result

def check(candidate):
    assert candidate({'a': 1, 'b': 2, 'c': 3, 'd': 2}) == {1: 'a', 2: 'd', 3: 'c'}

def test_check():
	check(f)