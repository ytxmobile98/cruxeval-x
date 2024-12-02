from typing import List, Dict, Tuple

def f(array: List[str]) -> List[str]:
    """"""
    ### Canonical solution below ###
    result = []
    for elem in array:
        if elem.isascii() or (isinstance(elem, int) and (not str(abs(elem)).isascii())):
            result.append(elem)
    return result

### Unit tests below ###
def check(candidate):
    assert candidate(['a', 'b', 'c']) == ['a', 'b', 'c']

def test_check():
    check(f)

