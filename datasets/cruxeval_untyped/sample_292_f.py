def f(text):
    """"""
    ### Canonical solution below ###
    new_text = [c if c.isdigit() else '*' for c in text]
    return ''.join(new_text)

def check(candidate):
    assert candidate('5f83u23saa') == '5*83*23***'

def test_check():
	check(f)