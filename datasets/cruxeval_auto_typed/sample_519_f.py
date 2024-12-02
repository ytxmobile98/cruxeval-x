from typing import List, Dict, Tuple

def f(d: Dict[None, None]) -> Dict[int, Union[bool, int]]:
    """"""
    ### Canonical solution below ###
    d['luck'] = 42
    d.clear()
    return {1: False, 2: 0}

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {1: False, 2: 0}

def test_check():
    check(f)

