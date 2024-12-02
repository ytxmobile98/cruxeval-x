from typing import List, Dict, Tuple

def f(array: List[int], list: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    array.extend(list)
    [e for e in array if e % 2 == 0]
    return [e for e in array if e >= 10]

### Unit tests below ###
def check(candidate):
    assert candidate([2, 15], [15, 1]) == [15, 15]

def test_check():
    check(f)

