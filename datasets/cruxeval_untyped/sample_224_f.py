def f(array, value):
    """"""
    ### Canonical solution below ###
    array.reverse()
    array.pop()
    odd = []
    while len(array) > 0:
        tmp = {}
        tmp[array.pop()] = value
        odd.append(tmp)
    result = {}
    while len(odd) > 0:
        result.update(odd.pop())
    return result

def check(candidate):
    assert candidate(['23'], 123) == {}

def test_check():
	check(f)