from typing import List, Dict, Tuple

def f(str: str) -> str:
    """"""
    ### Canonical solution below ###
    d = str.rpartition('ar')
    return ' '.join((d[0], d[1], d[2]))

### Unit tests below ###
def check(candidate):
    assert candidate('xxxarmmarxx') == 'xxxarmm ar xx'

def test_check():
    check(f)

