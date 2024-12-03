from typing import List, Dict, Tuple

def f(ls: List[Union[str, int]]) -> Dict[Union[str, int], int]:
    """"""
    ### Canonical solution below ###
    return dict.fromkeys(ls, 0)

### Unit tests below ###
def check(candidate):
    assert candidate(['x', 'u', 'w', 'j', 3, 6]) == {'x': 0, 'u': 0, 'w': 0, 'j': 0, 3: 0, 6: 0}

def test_check():
    check(f)
