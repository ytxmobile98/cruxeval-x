from typing import List, Dict, Tuple

def f(arr: List[str], d: Dict[None, None]) -> Dict[str, str]:
    """"""
    ### Canonical solution below ###
    for i in range(1, len(arr), 2):
        d.update({arr[i]: arr[i - 1]})
    return d

### Unit tests below ###
def check(candidate):
    assert candidate(['b', 'vzjmc', 'f', 'ae', '0'], dict()) == {'vzjmc': 'b', 'ae': 'f'}

def test_check():
    check(f)

