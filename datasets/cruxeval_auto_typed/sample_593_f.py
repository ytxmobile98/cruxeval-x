from typing import List, Dict, Tuple

def f(nums: List[None], n: int) -> List[None]:
    """"""
    ### Canonical solution below ###
    pos = len(nums) - 1
    for i in range(-len(nums), 0):
        nums.insert(pos, nums[i])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([], 14) == []

def test_check():
    check(f)

