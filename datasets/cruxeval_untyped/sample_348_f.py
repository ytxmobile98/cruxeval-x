def f(dictionary):
    """"""
    ### Canonical solution below ###
    return dictionary.copy()

def check(candidate):
    assert candidate({563: 555, 133: None}) == {563: 555, 133: None}

def test_check():
	check(f)