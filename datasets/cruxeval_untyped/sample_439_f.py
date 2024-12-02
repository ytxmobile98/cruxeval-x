def f(value):
    """"""
    ### Canonical solution below ###
    parts = value.partition(' ')[::2]
    return ''.join(parts)

def check(candidate):
    assert candidate('coscifysu') == 'coscifysu'

def test_check():
	check(f)