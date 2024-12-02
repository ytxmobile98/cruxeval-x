def f(arr, d):
    """"""
    ### Canonical solution below ###
    for i in range(1, len(arr), 2):
        d.update({arr[i]: arr[i-1]})

    return d

def check(candidate):
    assert candidate(['b', 'vzjmc', 'f', 'ae', '0'], dict()) == {'vzjmc': 'b', 'ae': 'f'}

def test_check():
	check(f)