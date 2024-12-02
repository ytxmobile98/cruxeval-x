from typing import List, Dict, Tuple

def f(d: Dict[Union[str, int], str], rm: List[int]) -> Dict[str, str]:
    """"""
    ### Canonical solution below ###
    res = d.copy()
    for k in rm:
        if k in res:
            del res[k]
    return res

### Unit tests below ###
def check(candidate):
    assert candidate({'1': 'a', 1: 'a', 1: 'b', '1': 'b'}, [1]) == {'1': 'b'}

def test_check():
    check(f)

