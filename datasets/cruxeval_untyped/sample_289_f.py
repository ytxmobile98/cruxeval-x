def f(code):
    """"""
    ### Canonical solution below ###
    return "{}: {}".format(code, code.encode())

def check(candidate):
    assert candidate('148') == "148: b'148'"

def test_check():
	check(f)