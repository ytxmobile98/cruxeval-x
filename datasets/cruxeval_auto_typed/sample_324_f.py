from typing import List, Dict, Tuple

def f(nums: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    (asc, desc) = (nums.copy(), [])
    asc.reverse()
    desc = asc[:len(asc) // 2]
    return desc + asc + desc

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

