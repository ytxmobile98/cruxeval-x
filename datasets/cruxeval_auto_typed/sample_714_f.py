from typing import List, Dict, Tuple

def f(array: List[int]) -> List[None]:
    """"""
    ### Canonical solution below ###
    array.reverse()
    array.clear()
    array.extend('x' * len(array))
    array.reverse()
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([3, -2, 0]) == []

def test_check():
    check(f)

