def f(text, chars):
    """"""
    ### Canonical solution below ###
    num_applies = 2
    extra_chars = ''
    for i in range(num_applies):
        extra_chars += chars
        text = text.replace(extra_chars, '')
    return text

def check(candidate):
    assert candidate('zbzquiuqnmfkx', 'mk') == 'zbzquiuqnmfkx'

def test_check():
	check(f)