from typing import List, Dict, Tuple

def f(numbers: range) -> List[None]:
    """"""
    ### Canonical solution below ###
    floats = [n % 1 for n in numbers]
    return floats if 1 in floats else []

### Unit tests below ###
def check(candidate):
    assert candidate(range(100, 120)) == []

def test_check():
    check(f)

