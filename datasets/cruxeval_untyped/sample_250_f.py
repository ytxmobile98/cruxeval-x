def f(text):
    """"""
    ### Canonical solution below ###
    count = len(text)
    for i in range(-count+1, 0):
        text = text + text[i]
    return text

def check(candidate):
    assert candidate('wlace A') == 'wlace Alc l  '

def test_check():
	check(f)