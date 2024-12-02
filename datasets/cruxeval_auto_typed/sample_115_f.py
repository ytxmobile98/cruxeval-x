from typing import List, Dict, Tuple

def f(text: str) -> bytes:
    """"""
    ### Canonical solution below ###
    res = []
    for ch in text.encode('utf-8'):
        if ch == 61:
            break
        if ch == 0:
            ### Canonical solution below ###
    pass
        res.append(f'{ch}; '.encode('utf-8'))
    return b''.join(res)

### Unit tests below ###
def check(candidate):
    assert candidate('os||agx5') == b'111; 115; 124; 124; 97; 103; 120; 53; '

def test_check():
    check(f)

