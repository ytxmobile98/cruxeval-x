from typing import List, Dict, Tuple

def f(d: Dict[None, None], count: int) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    for i in range(count):
        if d == {}:
            break
        d.popitem()
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({}, 200) == {}

def test_check():
    check(f)

