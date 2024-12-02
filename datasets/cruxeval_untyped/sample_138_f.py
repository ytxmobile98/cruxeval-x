def f(text, chars):
    """"""
    ### Canonical solution below ###
    listchars = list(chars)
    first = listchars.pop()
    for i in listchars:
        text = text[0:text.find(i)]+i+text[text.find(i)+1:]
    return text

def check(candidate):
    assert candidate('tflb omn rtt', 'm') == 'tflb omn rtt'

def test_check():
	check(f)