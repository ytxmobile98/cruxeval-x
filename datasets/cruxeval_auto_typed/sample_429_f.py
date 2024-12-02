from typing import List, Dict, Tuple

def f(d: Dict[Union[int, str, float], int]) -> List[Union[Tuple[float, int], Tuple[str, int], Tuple[int, int]]]:
    """"""
    ### Canonical solution below ###
    result = []
    while len(d.keys()) > 0:
        result.append(d.popitem())
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({5: 1, 'abc': 2, 'defghi': 2, 87.29: 3}) == [(87.29, 3), ('defghi', 2), ('abc', 2), (5, 1)]

def test_check():
    check(f)

