def f(dictionary):
    """"""
    ### Canonical solution below ###
    dictionary[1049] = 55
    key, value = dictionary.popitem()
    dictionary[key] = value
    return dictionary

def check(candidate):
    assert candidate({'noeohqhk': 623}) == {'noeohqhk': 623, 1049: 55}

def test_check():
	check(f)