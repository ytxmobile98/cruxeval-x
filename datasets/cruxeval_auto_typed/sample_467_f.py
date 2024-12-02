from typing import List, Dict, Tuple

def f(nums: Dict[None, None]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    copy = nums.copy()
    newDict = dict()
    for k in copy:
        newDict[k] = len(copy[k])
    return newDict

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)

