def f(obj):
    """"""
    ### Canonical solution below ###
    for k, v in obj.items():
        if v >= 0:
            obj[k] = -v
    return obj

def check(candidate):
    assert candidate({'R': 0, 'T': 3, 'F': -6, 'K': 0}) == {'R': 0, 'T': -3, 'F': -6, 'K': 0}

def test_check():
	check(f)