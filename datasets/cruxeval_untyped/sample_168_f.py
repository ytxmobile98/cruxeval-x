def f(text, new_value, index):
    """"""
    ### Canonical solution below ###
    key = text.maketrans(text[index], new_value)
    return text.translate(key)

def check(candidate):
    assert candidate('spain', 'b', 4) == 'spaib'

def test_check():
	check(f)