from typing import List, Dict, Tuple

def f(cart: Dict[None, None]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    while len(cart) > 5:
        cart.popitem()
    return cart

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)

