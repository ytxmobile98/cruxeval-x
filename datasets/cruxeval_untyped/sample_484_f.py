def f(arr):
    """"""
    ### Canonical solution below ###
    result = []
    for item in arr:
        try:
            if item.isnumeric():
                result.append(int(item)*2)
        except ValueError:
            result.append(item[::-1])
    return result

def check(candidate):
    assert candidate(['91', '16', '6r', '5r', 'egr', '', 'f', 'q1f', '-2']) == [182, 32]

def test_check():
	check(f)