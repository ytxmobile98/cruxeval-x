from typing import List, Dict, Tuple

def f(nums: List[int]) -> List[None]:
    """"""
    ### Canonical solution below ###
    nums.clear()
    for num in nums:
        nums.append(num * 2)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([4, 3, 2, 1, 2, -1, 4, 2]) == []

def test_check():
    check(f)

