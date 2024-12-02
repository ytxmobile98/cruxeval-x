from typing import List, Dict, Tuple

def f(aDict: Dict[int, int]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    return dict([v for v in aDict.items()])

### Unit tests below ###
def check(candidate):
    assert candidate({1: 1, 2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}

def test_check():
    check(f)

