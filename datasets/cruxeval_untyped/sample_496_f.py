def f(text, value):
    """"""
    ### Canonical solution below ###
    if isinstance(value, str):
        return text.count(value) + text.count(value.lower())
    return text.count(value)

def check(candidate):
    assert candidate('eftw{ьТсk_1', '\\') == 0

def test_check():
	check(f)