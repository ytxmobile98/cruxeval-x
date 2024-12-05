from typing import List, Dict, Tuple

def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return ''.join([c for c in s if c.isspace()])

### Unit tests below ###
def check(candidate):
    assert candidate('\ngiyixjkvu\n\r\r \x0crgjuo') == '\n\n\r\r \x0c'

def test_check():
    check(f)
