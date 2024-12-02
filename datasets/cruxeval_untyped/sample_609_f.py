def f(array, elem):
    """"""
    ### Canonical solution below ###
    result = array.copy()
    while result:
        key, value = result.popitem()
        if elem == key or elem == value:
            result.update(array)
        del result[key]
    return result

def check(candidate):
    assert candidate({}, 1) == {}

def test_check():
	check(f)