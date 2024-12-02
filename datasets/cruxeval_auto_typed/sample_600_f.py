from typing import List, Dict, Tuple

def f(array: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    just_ns = list(map(lambda num: 'n' * num, array))
    final_output = []
    for wipe in just_ns:
        final_output.append(wipe)
    return final_output

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

