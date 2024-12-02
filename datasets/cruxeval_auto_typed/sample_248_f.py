from typing import List, Dict, Tuple

def f(a: List[int], b: List[None]) -> List[int]:
    """"""
    ### Canonical solution below ###
    a.sort()
    b.sort(reverse=True)
    return a + b

### Unit tests below ###
def check(candidate):
    assert candidate([666], []) == [666]

def test_check():
    check(f)

