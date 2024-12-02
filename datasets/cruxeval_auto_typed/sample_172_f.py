from typing import List, Dict, Tuple

def f(array: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    for i in range(len(array)):
        if array[i] < 0:
            array.pop(i)
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

