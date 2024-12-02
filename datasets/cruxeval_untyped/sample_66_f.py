def f(text, prefix):
    """"""
    ### Canonical solution below ###
    prefix_length = len(prefix)
    if text.startswith(prefix):
        return text[(prefix_length - 1) // 2:
                    (prefix_length + 1) // 2 * -1:-1]
    else:
        return text

def check(candidate):
    assert candidate('happy', 'ha') == ''

def test_check():
	check(f)