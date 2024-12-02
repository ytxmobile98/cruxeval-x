from typing import List, Dict, Tuple

def f(d: Dict[str, Union[int, str]]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    d.clear()
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({'a': 3, 'b': -1, 'c': 'Dum'}) == {}

def test_check():
    check(f)

