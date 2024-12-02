def f(a, b):
    """"""
    ### Canonical solution below ###
    return {**a, **b}

def check(candidate):
    assert candidate({'w': 5, 'wi': 10}, {'w': 3}) == {'w': 3, 'wi': 10}

def test_check():
	check(f)