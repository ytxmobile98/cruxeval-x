def f(d):
    """"""
    ### Canonical solution below ###
    result = {}
    for ki, li in d.items():
        result.update({ki: []})
        for kj, dj in enumerate(li):
            result[ki].append({})
            for kk, l in dj.items():
                result[ki][kj][kk] = l.copy()
    return result

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)