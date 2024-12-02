from typing import List, Dict, Tuple

def f(str: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    base = char * (str.count(char) + 1)
    return str.removesuffix(base)

### Unit tests below ###
def check(candidate):
    assert candidate('mnmnj krupa...##!@#!@#$$@##', '@') == 'mnmnj krupa...##!@#!@#$$@##'

def test_check():
    check(f)

