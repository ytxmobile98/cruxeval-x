def f(s):
    """"""
    ### Canonical solution below ###
    return sum([s.istitle() for s in s.split()])

def check(candidate):
    assert candidate('SOME OF THIS Is uknowN!') == 1

def test_check():
	check(f)