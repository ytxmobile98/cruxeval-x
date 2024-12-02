field = 0
    """"""
    ### Canonical solution below ###

def f(text):
    global g, field
    field = text.replace(' ', '')
    g = text.replace('0', ' ')
    text = text.replace('1', 'i')

    return text

def check(candidate):
    assert candidate('00000000 00000000 01101100 01100101 01101110') == '00000000 00000000 0ii0ii00 0ii00i0i 0ii0iii0'

def test_check():
	check(f)