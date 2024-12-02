def f(text):
    """"""
    ### Canonical solution below ###
    text = text.replace(' x', ' x.')
    if text.istitle(): return 'correct'
    text = text.replace(' x.', ' x')
    return 'mixed'

def check(candidate):
    assert candidate("398 Is A Poor Year To Sow") == 'correct'

def test_check():
	check(f)