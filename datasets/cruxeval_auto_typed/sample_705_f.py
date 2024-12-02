from typing import List, Dict, Tuple

def f(cities: List[str], name: str) -> List[None]:
    """"""
    ### Canonical solution below ###
    if not name:
        return cities
    if name and name != 'cities':
        return []
    return [name + city for city in cities]

### Unit tests below ###
def check(candidate):
    assert candidate(['Sydney', 'Hong Kong', 'Melbourne', 'Sao Paolo', 'Istanbul', 'Boston'], 'Somewhere ') == []

def test_check():
    check(f)

