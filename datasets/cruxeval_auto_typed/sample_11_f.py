from typing import List, Dict, Tuple

def f(a: Dict[None, None], b: Dict[str, str]) -> Dict[str, List[str]]:
    """"""
    ### Canonical solution below ###
    for (key, value) in b.items():
        if key not in a:
            a[key] = [value]
        else:
            a[key].append(value)
    return a

### Unit tests below ###
def check(candidate):
    assert candidate({}, {'foo': 'bar'}) == {'foo': ['bar']}

def test_check():
    check(f)
