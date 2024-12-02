from typing import List, Dict, Tuple

def f(ets: Dict[None, None]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    while ets:
        (k, v) = ets.popitem()
        ets[k] = v ** 2
    return ets

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)

