def f(counts):
    """"""
    ### Canonical solution below ###
    dict = {}
    for k, v in counts.items():
        count = counts[k]
        if count not in dict:
            dict[count] = []
        dict[count].append(k)
    counts.update(dict)
    return counts

def check(candidate):
    assert candidate({'2': 2, '0': 1, '1': 2}) == {'2': 2, '0': 1, '1': 2, 2: ['2', '1'], 1: ['0']}

def test_check():
	check(f)