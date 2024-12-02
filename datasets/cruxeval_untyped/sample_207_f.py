def f(commands):
    """"""
    ### Canonical solution below ###
    d = {}
    for c in commands:
        d.update(c)
    return d

def check(candidate):
    assert candidate([{"brown": 2}, {"blue": 5}, {"bright": 4}]) == {'brown': 2, 'blue': 5, 'bright': 4}

def test_check():
	check(f)