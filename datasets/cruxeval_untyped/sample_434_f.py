def f(string):
    """"""
    ### Canonical solution below ###
    try:
       return string.rfind('e')
    except AttributeError:
        return "Nuk"

def check(candidate):
    assert candidate('eeuseeeoehasa') == 8

def test_check():
	check(f)