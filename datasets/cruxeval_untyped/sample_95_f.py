def f(zoo):
    """"""
    ### Canonical solution below ###
    return dict((v, k) for k, v in zoo.items())

def check(candidate):
    assert candidate({'AAA': 'fr'}) == {'fr': 'AAA'}

def test_check():
	check(f)