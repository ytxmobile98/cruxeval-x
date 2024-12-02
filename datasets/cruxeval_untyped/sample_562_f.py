def f(text):
    """"""
    ### Canonical solution below ###
    return text.upper() == str(text)

def check(candidate):
    assert candidate('VTBAEPJSLGAHINS') == True

def test_check():
	check(f)