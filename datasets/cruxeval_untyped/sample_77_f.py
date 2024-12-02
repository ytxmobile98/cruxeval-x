def f(text, character):
    """"""
    ### Canonical solution below ###
    subject = text[text.rfind(character):]
    return subject*text.count(character)

def check(candidate):
    assert candidate('h ,lpvvkohh,u', 'i') == ''

def test_check():
	check(f)