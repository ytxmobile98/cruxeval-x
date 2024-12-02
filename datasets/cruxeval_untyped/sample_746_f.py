def f(dct):
    """"""
    ### Canonical solution below ###
    values = dct.values()
    result = {}
    for value in values:
        item = value.split('.')[0]+'@pinc.uk'
        result[value] = item
    return result

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)