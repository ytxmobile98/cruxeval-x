from typing import List, Dict, Tuple

def f(array: List[None], arr: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    result = []
    for s in arr:
        result += list(filter(lambda l: l != '', s.split(arr[array.index(s)])))
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([], []) == []

def test_check():
    check(f)

