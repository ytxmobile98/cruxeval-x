def f(text):
    """"""
    ### Canonical solution below ###
    return text.replace('\\"', '"')

def check(candidate):
    assert candidate('Because it intrigues them') == 'Because it intrigues them'

def test_check():
	check(f)