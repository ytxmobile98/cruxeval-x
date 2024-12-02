def f(text):
    """"""
    ### Canonical solution below ###
    string_a, string_b = text.split(',')
    return -(len(string_a) + (len(string_b)))

def check(candidate):
    assert candidate('dog,cat') == -6

def test_check():
	check(f)