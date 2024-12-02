def f(values):
    """"""
    ### Canonical solution below ###
    names = ['Pete', 'Linda', 'Angela']
    names.extend(values)
    names.sort()
    return names

def check(candidate):
    assert candidate(['Dan', 'Joe', 'Dusty']) == ['Angela', 'Dan', 'Dusty', 'Joe', 'Linda', 'Pete']

def test_check():
	check(f)