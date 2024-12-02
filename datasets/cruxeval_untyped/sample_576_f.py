def f(array, const):
    """"""
    ### Canonical solution below ###
    output = ['x']
    for i in range(1, len(array) + 1):
        if i % 2 != 0:
            output.append(array[i - 1] * -2)
        else:
            output.append(const)
    return output

def check(candidate):
    assert candidate([1, 2, 3], -1) == ['x', -2, -1, -6]

def test_check():
	check(f)