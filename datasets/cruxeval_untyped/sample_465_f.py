def f(seq, value):
    """"""
    ### Canonical solution below ###
    roles = dict.fromkeys(seq, 'north')
    if value:
        roles.update(key.strip() for key in value.split(', '))
    return roles

def check(candidate):
    assert candidate(['wise king', 'young king'], '') == {'wise king': 'north', 'young king': 'north'}

def test_check():
	check(f)