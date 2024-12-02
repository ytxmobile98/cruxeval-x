from typing import List, Dict, Tuple

def f(list: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if List[j] > List[j + 1]:
                (List[j], List[j + 1]) = (List[j + 1], List[j])
                list.sort()
    return list

### Unit tests below ###
def check(candidate):
    assert candidate([63, 0, 1, 5, 9, 87, 0, 7, 25, 4]) == [0, 0, 1, 4, 5, 7, 9, 25, 63, 87]

def test_check():
    check(f)

