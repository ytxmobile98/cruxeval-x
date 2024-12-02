def f(text, value):
    """"""
    ### Canonical solution below ###
    return text.removeprefix(value.lower())

def check(candidate):
    assert candidate('coscifysu', 'cos') == 'cifysu'

def test_check():
	check(f)