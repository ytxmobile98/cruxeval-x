from typing import List, Dict, Tuple

def f(items: Tuple[int, int, int, int, int, int, int, int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    items = list(items)
    odd_positioned = []
    while len(items) > 0:
        position = items.index(min(items))
        items.pop(position)
        item = items.pop(position)
        odd_positioned.append(item)
    return odd_positioned

### Unit tests below ###
def check(candidate):
    assert candidate((1, 2, 3, 4, 5, 6, 7, 8)) == [2, 4, 6, 8]

def test_check():
    check(f)

