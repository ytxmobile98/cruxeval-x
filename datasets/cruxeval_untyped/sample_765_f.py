def f(text):
    """"""
    ### Canonical solution below ###
    return sum(1 for c in text if c.isdigit())

def check(candidate):
    assert candidate('so456') == 3

def test_check():
	check(f)