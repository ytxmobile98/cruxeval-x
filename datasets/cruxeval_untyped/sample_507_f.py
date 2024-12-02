def f(text, search):
    """"""
    ### Canonical solution below ###
    result = text.lower()
    return result.find(search.lower())

def check(candidate):
    assert candidate('car hat', 'car') == 0

def test_check():
	check(f)