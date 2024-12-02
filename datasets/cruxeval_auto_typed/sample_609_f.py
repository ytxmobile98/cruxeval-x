from typing import List, Dict, Tuple

def f(array: Dict[None, None], elem: int) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    result = array.copy()
    while result:
        (key, value) = result.popitem()
        if elem == key or elem == value:
            result.update(array)
        del result[key]
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({}, 1) == {}

def test_check():
    check(f)

