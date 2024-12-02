from typing import List, Dict, Tuple

def f(array: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    a = []
    array.reverse()
    for i in range(len(array)):
        if array[i] != 0:
            a.append(array[i])
    a.reverse()
    return a

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

