from typing import List, Dict, Tuple

def f(stg: str, tabs: Tuple[str, str, str, str, str, str, str, str]) -> str:
    """"""
    ### Canonical solution below ###
    for tab in tabs:
        stg = stg.rstrip(tab)
    return stg

### Unit tests below ###
def check(candidate):
    assert candidate('31849 let it!31849 ### Canonical solution below ###
    pass!', ('3', '1', '8', ' ', '1', '9', '2', 'd')) == '31849 let it!31849 ### Canonical solution below ###
    pass!'

def test_check():
    check(f)

