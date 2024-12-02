def f(cart):
    """"""
    ### Canonical solution below ###
    while len(cart) > 5:
        cart.popitem()
    return cart

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)