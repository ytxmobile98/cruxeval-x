def f(text, chars):
    """"""
    ### Canonical solution below ###
    if chars:
        text = text.rstrip(chars)
    else:
        text = text.rstrip(' ')
    if text == '':
        return '-'
    return text

def check(candidate):
    assert candidate('new-medium-performing-application - XQuery 2.2', '0123456789-') == 'new-medium-performing-application - XQuery 2.'

def test_check():
	check(f)