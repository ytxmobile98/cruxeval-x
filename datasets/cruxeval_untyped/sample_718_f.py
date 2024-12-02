def f(text):
    """"""
    ### Canonical solution below ###
    t = text
    for i in text:
        text = text.replace(i, '')
    return str(len(text)) + t

def check(candidate):
    assert candidate('ThisIsSoAtrocious') == '0ThisIsSoAtrocious'

def test_check():
	check(f)