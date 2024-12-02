def f(test, sep, maxsplit):
    """"""
    ### Canonical solution below ###
    try:
        return test.rsplit(sep, maxsplit)
    except:
        return test.rsplit()

def check(candidate):
    assert candidate('ab cd', 'x', 2) == ['ab cd']

def test_check():
	check(f)