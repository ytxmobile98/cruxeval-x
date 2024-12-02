def f(array, arr):
    """"""
    ### Canonical solution below ###
    result = []
    for s in arr:
        result += list(filter(lambda l: l != '', s.split(arr[array.index(s)])))
    return result

def check(candidate):
    assert candidate([], []) == []

def test_check():
	check(f)