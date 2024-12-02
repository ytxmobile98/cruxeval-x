from typing import List, Dict, Tuple

def f(nums: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    for i in range(len(nums)):
        if not i % 2:
            nums.append(nums[i] * nums[i + 1])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

