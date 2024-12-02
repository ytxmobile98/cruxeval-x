from typing import List, Dict, Tuple

def f(vectors: List[None]) -> List[None]:
    """"""
    ### Canonical solution below ###
    sorted_vecs = []
    for vec in vectors:
        vec.sort()
        sorted_vecs.append(vec)
    return sorted_vecs

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)

