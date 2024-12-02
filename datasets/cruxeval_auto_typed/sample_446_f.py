from typing import List, Dict, Tuple

def f(array: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    l = len(array)
    if l % 2 == 0:
        array.clear()
    else:
        array.reverse()
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

