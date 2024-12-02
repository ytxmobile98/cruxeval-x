def f(array):
    """"""
    ### Canonical solution below ###
    prev = array[0]
    newArray = array[:]
    for i in range(1, len(array)):
        if prev != array[i]:
            newArray[i] = array[i]
        else:
            del newArray[i]
        prev = array[i]
    return newArray

def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]

def test_check():
	check(f)