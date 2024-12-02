def f(text, new_ending):
    """"""
    ### Canonical solution below ###
    result = list(text)
    result.extend(new_ending)
    return ''.join(result)

def check(candidate):
    assert candidate('jro', 'wdlp') == 'jrowdlp'

def test_check():
	check(f)