from typing import List, Dict, Tuple

def f(price: float, product: str) -> float:
    """"""
    ### Canonical solution below ###
    inventory = ['olives', 'key', 'orange']
    if product not in inventory:
        return price
    else:
        price *= 0.85
        inventory.remove(product)
    return price

### Unit tests below ###
def check(candidate):
    assert candidate(8.5, 'grapes') == 8.5

def test_check():
    check(f)

