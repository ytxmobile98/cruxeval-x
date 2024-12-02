from typing import List, Dict, Tuple

def f(a: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    if a == 0:
        return [0]
    result = []
    while a > 0:
        result.append(a % 10)
        a = a // 10
    result.reverse()
    return int(''.join((str(i) for i in result)))

### Unit tests below ###
def check(candidate):
    assert candidate(0) == [0]

def test_check():
    check(f)

