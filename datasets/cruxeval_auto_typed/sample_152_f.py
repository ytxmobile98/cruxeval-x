from typing import List, Dict, Tuple

def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    n = 0
    for char in text:
        if char.isupper():
            n += 1
    return n

### Unit tests below ###
def check(candidate):
    assert candidate(''.join(['A'] * 20)) == 20

def test_check():
    check(f)

