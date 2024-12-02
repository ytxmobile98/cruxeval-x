from typing import List, Dict, Tuple

def f(text: str, encoding: str) -> bytes:
    """"""
    ### Canonical solution below ###
    try:
        return text.encode(encoding)
    except LookupError:
        return str(LookupError)

### Unit tests below ###
def check(candidate):
    assert candidate('13:45:56', 'shift_jis') == b'13:45:56'

def test_check():
    check(f)

