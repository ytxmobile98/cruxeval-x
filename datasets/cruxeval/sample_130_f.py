from typing import Dict

def f(m: Dict[str, int]) -> str:
    """"""
    ### Canonical solution below ###
    items = list(m.items())
    for i in range(len(items)-2, -1, -1):
        tmp = items[i]
        items[i] = items[i+1] 
        items[i+1] = tmp
    return ['{}={}', '{1}={0}'][len(items) % 2].format(
        *m.keys(), **m
    )

### Unit tests below ###
def check(candidate):
    assert candidate({'l':4, 'h':6, 'o':9}) == 'h=l'

def test_check():
    check(f)