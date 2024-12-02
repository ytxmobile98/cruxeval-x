from typing import List, Dict, Tuple

def f(array: List[Union[List[int], List[None]]]) -> List[Union[List[int], List[None]]]:
    """"""
    ### Canonical solution below ###
    return_arr = []
    for a in array:
        return_arr.append(a.copy())
    return return_arr

### Unit tests below ###
def check(candidate):
    assert candidate([[1, 2, 3], [], [1, 2, 3]]) == [[1, 2, 3], [], [1, 2, 3]]

def test_check():
    check(f)

