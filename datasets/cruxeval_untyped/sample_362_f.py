def f(text):
    """"""
    ### Canonical solution below ###
    for i in range(len(text)-1):
        if text[i:].islower():
            return text[i + 1:]
    return ''

def check(candidate):
    assert candidate('wrazugizoernmgzu') == 'razugizoernmgzu'

def test_check():
	check(f)