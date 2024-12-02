def f(text, letter):
    """"""
    ### Canonical solution below ###
    if letter in text:
        start = text.index(letter)
        return text[start + 1:] + text[:start + 1]
    return text

def check(candidate):
    assert candidate('19kefp7', '9') == 'kefp719'

def test_check():
	check(f)