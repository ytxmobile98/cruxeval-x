def f(string, numbers):
    """"""
    ### Canonical solution below ###
    arr = []
    for num in numbers:
        arr.append(string.zfill(num))
    return ' '.join(arr)

def check(candidate):
    assert candidate('4327', [2, 8, 9, 2, 7, 1]) == '4327 00004327 000004327 4327 0004327 4327'

def test_check():
	check(f)