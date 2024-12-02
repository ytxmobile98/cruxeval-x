from typing import List, Dict, Tuple

def f(test: str, sep: str, maxsplit: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    try:
        return test.rsplit(sep, maxsplit)
    except:
        return test.rsplit()

### Unit tests below ###
def check(candidate):
    assert candidate('ab cd', 'x', 2) == ['ab cd']

def test_check():
    check(f)

