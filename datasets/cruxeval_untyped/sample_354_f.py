def f(description, values):
    """"""
    ### Canonical solution below ###
    if values[1] is None:
        values = values[0:1]
    else:
        values = values[1:]
    return description.format(*values)

def check(candidate):
    assert candidate('{0}, {0}!!!', ['R', None]) == 'R, R!!!'

def test_check():
	check(f)