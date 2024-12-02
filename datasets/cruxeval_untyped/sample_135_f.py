def f():
    """"""
    ### Canonical solution below ###
    d = {
        'Russia': [('Moscow', 'Russia'), ('Vladivostok', 'Russia')],
        'Kazakhstan': [('Astana', 'Kazakhstan')],
    }
    return list(d.keys())

def check(candidate):
    assert candidate() == ['Russia', 'Kazakhstan']

def test_check():
	check(f)