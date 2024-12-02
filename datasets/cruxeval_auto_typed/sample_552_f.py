from typing import List, Dict, Tuple

def f(d: Dict[int, Union[float, List[int]]]) -> Dict[int, Union[float, List[int]]]:
    """"""
    ### Canonical solution below ###
    result = {}
    for (k, v) in d.items():
        if isinstance(k, float):
            for i in v:
                result[i] = k
        else:
            result[k] = v
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({2: 0.76, 5: [3, 6, 9, 12]}) == {2: 0.76, 5: [3, 6, 9, 12]}

def test_check():
    check(f)

