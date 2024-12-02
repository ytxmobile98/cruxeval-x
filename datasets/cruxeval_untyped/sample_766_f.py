def f(values, value):
    """"""
    ### Canonical solution below ###
    length = len(values)
    new_dict = dict.fromkeys(values, value)
    new_dict[''.join(sorted(values))] = value * 3
    return new_dict

def check(candidate):
    assert candidate(['0','3'], 117) == {'0': 117, '3': 117, '03': 351}

def test_check():
	check(f)