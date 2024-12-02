from typing import List, Dict, Tuple

def f(alphabet: str, s: str) -> List[None]:
    """"""
    ### Canonical solution below ###
    a = [x for x in alphabet if x.upper() in s]
    if s.upper() == s:
        a.append('all_uppercased')
    return a

### Unit tests below ###
def check(candidate):
    assert candidate('abcdefghijklmnopqrstuvwxyz', 'uppercased # % ^ @ ! vz.') == []

def test_check():
    check(f)

