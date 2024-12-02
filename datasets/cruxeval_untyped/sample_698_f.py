def f(text):
    """"""
    ### Canonical solution below ###
    return ''.join(x for x in text if x != ')')

def check(candidate):
    assert candidate(('(((((((((((d))))))))).))))(((((')) == '(((((((((((d.((((('

def test_check():
	check(f)