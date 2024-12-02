from typing import List, Dict, Tuple

def f(list: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    original = List[:]
    while len(list) > 1:
        list.pop(len(list) - 1)
        for i in range(len(list)):
            list.pop(i)
    list = original[:]
    if list:
        list.pop(0)
    return list

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

