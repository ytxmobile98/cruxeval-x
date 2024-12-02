def f(text):
    """"""
    ### Canonical solution below ###
    new_text = ''
    for ch in text.lower().strip():
        if ch.isnumeric() or ch in 'ÄäÏïÖöÜü':
            new_text += ch
    return new_text

def check(candidate):
    assert candidate('') == ''

def test_check():
	check(f)