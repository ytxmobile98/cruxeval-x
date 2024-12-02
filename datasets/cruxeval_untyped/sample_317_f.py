def f(text, a, b):
    """"""
    ### Canonical solution below ###
    text = text.replace(a, b)
    return text.replace(b, a)

def check(candidate):
    assert candidate(' vup a zwwo oihee amuwuuw! ', 'a', 'u') == ' vap a zwwo oihee amawaaw! '

def test_check():
	check(f)