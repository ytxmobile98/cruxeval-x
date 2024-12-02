from typing import List, Dict, Tuple

def f(a: Tuple[int], b: Tuple[int], c: Tuple[int, int]) -> Dict[int, NoneType]:
    """"""
    ### Canonical solution below ###
    result = {}
    for d in (a, b, c):
        result.update(dict.fromkeys(d))
    return result

### Unit tests below ###
def check(candidate):
    assert candidate((1,), (1,), (1, 2)) == {1: None, 2: None}

def test_check():
    check(f)

