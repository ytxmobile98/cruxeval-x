def f(text, x):
    """"""
    ### Canonical solution below ###
    if text.removeprefix(x) == text:
        return f(text[1:], x)
    else:
        return text

def check(candidate):
    assert candidate("Ibaskdjgblw asdl ", "djgblw") == 'djgblw asdl '

def test_check():
	check(f)