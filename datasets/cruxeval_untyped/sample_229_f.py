def f(dic, value):
    """"""
    ### Canonical solution below ###
    result = []
    for e in dic:
        result.append(e[0])
        if e[1] == value:
            result.reverse()
        else:
            result.append(e[1])
    return result

def check(candidate):
    assert candidate({'9m':2, 'mA':1, '10K':2, 'Lk':2}, 1) == ['9', 'm', 'm', 'A', '1', '0', 'L', 'k']

def test_check():
	check(f)