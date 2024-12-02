from typing import List, Dict, Tuple

def f(d: Dict[None, None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    result = [None] * len(d)
    a = b = 0
    while d:
        result[a] = d.popitem(a == b)
        (a, b) = (b, (b + 1) % len(result))
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({}) == []

def test_check():
    check(f)

