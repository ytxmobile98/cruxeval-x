from typing import List, Dict, Tuple

def f(text: str, sub: str) -> List[None]:
    """"""
    ### Canonical solution below ###
    index = []
    starting = 0
    while starting != -1:
        starting = text.find(sub, starting)
        if starting != -1:
            index.append(starting)
            starting += len(sub)
    return index

### Unit tests below ###
def check(candidate):
    assert candidate('egmdartoa', 'good') == []

def test_check():
    check(f)

