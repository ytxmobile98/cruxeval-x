def f(fields, update_dict):
    """"""
    ### Canonical solution below ###
    di = dict((x, '') for x in fields)
    di.update(update_dict)
    return di

def check(candidate):
    assert candidate(('ct', 'c', 'ca'), {'ca': 'cx'}) == {'ct': '', 'c': '', 'ca': 'cx'}

def test_check():
	check(f)