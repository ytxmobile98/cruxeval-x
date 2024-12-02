def f(array):
    """"""
    ### Canonical solution below ###
    a = []
    array.reverse()
    for i in range(len(array)):
        if array[i] != 0:
            a.append(array[i])
    a.reverse()
    return a

def check(candidate):
    assert candidate([]) == []

def test_check():
	check(f)