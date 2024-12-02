from typing import List, Dict, Tuple

def f(strings: List[str], substr: str) -> List[None]:
    """"""
    ### Canonical solution below ###
    list = [s for s in strings if s.startswith(substr)]
    return sorted(list, key=len)

### Unit tests below ###
def check(candidate):
    assert candidate(['condor', 'eyes', 'gay', 'isa'], 'd') == []

def test_check():
    check(f)

