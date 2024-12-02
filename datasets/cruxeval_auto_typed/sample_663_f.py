from typing import List, Dict, Tuple

def f(container: List[None], cron: int) -> List[None]:
    """"""
    ### Canonical solution below ###
    if not cron in container:
        return container
    pref = container[:container.index(cron)].copy()
    suff = container[container.index(cron) + 1:].copy()
    return pref + suff

### Unit tests below ###
def check(candidate):
    assert candidate([], 2) == []

def test_check():
    check(f)

