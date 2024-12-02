from typing import List, Dict, Tuple

def f(list: List[int], operation: function) -> List[int]:
    """"""
    ### Canonical solution below ###
    new_list = List[:]
    new_list.sort()
    operation(new_list)
    return list

### Unit tests below ###
def check(candidate):
    assert candidate([6, 4, 2, 8, 15], lambda x: x.reverse()) == [6, 4, 2, 8, 15]

def test_check():
    check(f)

