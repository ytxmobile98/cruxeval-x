from typing import List, Dict, Tuple

def f(str: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    if len(str) < n:
        return str
    else:
        return str.removeprefix(str[:n])

### Unit tests below ###
def check(candidate):
    assert candidate('try.', 5) == 'try.'

def test_check():
    check(f)

