from typing import List, Dict, Tuple

def f(data: Dict[int, int], num: int) -> List[Union[Tuple[int, int], Tuple[Tuple[int, int], NoneType]]]:
    """"""
    ### Canonical solution below ###
    new_dict = {}
    temp = list(data.items())
    for i in range(len(temp) - 1, num - 1, -1):
        new_Dict[temp[i]] = None
    return temp[num:] + list(new_dict.items())

### Unit tests below ###
def check(candidate):
    assert candidate({1: 9, 2: 10, 3: 1}, 1) == [(2, 10), (3, 1), ((3, 1), None), ((2, 10), None)]

def test_check():
    check(f)

