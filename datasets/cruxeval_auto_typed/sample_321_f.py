from typing import List, Dict, Tuple

def f(update: Dict[None, None], starting: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    d = starting.copy()
    for k in update:
        if k in d:
            d[k] += update[k]
        else:
            d[k] = update[k]
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({}, {'desciduous': 2}) == {'desciduous': 2}

def test_check():
    check(f)
