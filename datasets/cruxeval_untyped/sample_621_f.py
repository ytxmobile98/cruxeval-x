def f(text, encoding):
    """"""
    ### Canonical solution below ###
    try:
        return text.encode(encoding)
    except LookupError:
        return str(LookupError)

def check(candidate):
    assert candidate('13:45:56', 'shift_jis') == b'13:45:56'

def test_check():
	check(f)