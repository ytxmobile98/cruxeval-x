def f(text, elem):
    """"""
    ### Canonical solution below ###
    if elem != '':
        while text.startswith(elem):
            text = text.replace(elem, '')
        while elem.startswith(text):
            elem = elem.replace(text, '')
    return [elem, text]

def check(candidate):
    assert candidate("some", "1") == ['1', 'some']

def test_check():
	check(f)