from typing import List, Dict, Tuple

def f(d: Dict[str, Union[int, str]]) -> Tuple[bool, bool]:
    """"""
    ### Canonical solution below ###
    r = {'c': d.copy(), 'd': d.copy()}
    return (r['c'] is r['d'], r['c'] == r['d'])

### Unit tests below ###
def check(candidate):
    assert candidate({'i': 1, 'love': 'parakeets'}) == (False, True)

def test_check():
    check(f)

