from typing import List, Dict, Tuple

def f(out: str, mapping: Dict[None, None]) -> str:
    """"""
    ### Canonical solution below ###
    for key in mapping:
        out.format_map(mapping)
        if len(re.findall('{\\w}', out)) == 0:
            break
        mapping[key][1] = mapping[key][1][::-1]
    return out

### Unit tests below ###
def check(candidate):
    assert candidate('{{{{}}}}', {}) == '{{{{}}}}'

def test_check():
    check(f)

