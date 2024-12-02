def f(dict1, dict2):
    """"""
    ### Canonical solution below ###
    result = dict1.copy()
    result.update([(__, dict2[__]) for __ in dict2])
    return result

def check(candidate):
    assert candidate({'disface': 9, 'cam': 7}, {'mforce': 5}) == {'disface': 9, 'cam': 7, 'mforce': 5}

def test_check():
	check(f)