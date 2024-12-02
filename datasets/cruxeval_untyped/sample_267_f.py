def f(text, space):
    """"""
    ### Canonical solution below ###
    if space < 0:
        return text
    return text.ljust(len(text) // 2 + space)

def check(candidate):
    assert candidate('sowpf', -7) == 'sowpf'

def test_check():
	check(f)