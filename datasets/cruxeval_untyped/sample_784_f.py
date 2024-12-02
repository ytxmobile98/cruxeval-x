def f(key, value):
    """"""
    ### Canonical solution below ###
    dict_ = {key: value}
    return dict.popitem(dict_)

def check(candidate):
    assert candidate('read', 'Is') == ('read', 'Is')

def test_check():
	check(f)