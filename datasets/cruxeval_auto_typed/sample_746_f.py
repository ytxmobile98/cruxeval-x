from typing import List, Dict, Tuple

def f(dct: Dict[None, None]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    values = dct.values()
    result = {}
    for value in values:
        item = value.split('.')[0] + '@pinc.uk'
        result[value] = item
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)

