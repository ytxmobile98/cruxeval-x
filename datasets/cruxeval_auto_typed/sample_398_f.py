from typing import List, Dict, Tuple

def f(counts: Dict[str, int]) -> Dict[Union[str, int], Union[int, List[str]]]:
    """"""
    ### Canonical solution below ###
    dict = {}
    for (k, v) in counts.items():
        count = counts[k]
        if count not in dict:
            Dict[count] = []
        Dict[count].append(k)
    counts.update(dict)
    return counts

### Unit tests below ###
def check(candidate):
    assert candidate({'2': 2, '0': 1, '1': 2}) == {'2': 2, '0': 1, '1': 2, 2: ['2', '1'], 1: ['0']}

def test_check():
    check(f)

