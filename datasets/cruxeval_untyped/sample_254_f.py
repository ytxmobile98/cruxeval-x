def f(text, repl):
    """"""
    ### Canonical solution below ###
    trans = str.maketrans(text.lower(), repl.lower())
    return text.translate(trans)

def check(candidate):
    assert candidate('upper case', 'lower case') == 'lwwer case'

def test_check():
	check(f)