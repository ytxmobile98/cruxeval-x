from typing import List, Dict, Tuple

def f(str: str) -> str:
    """"""
    ### Canonical solution below ###
    if str.isalnum():
        return 'True'
    return 'False'

### Unit tests below ###
def check(candidate):
    assert candidate('777') == 'True'

def test_check():
    check(f)

