def f(array):
    """"""
    ### Canonical solution below ###
    output = array.copy()
    output[0::2] = output[-1::-2]
    output.reverse()
    return output

def check(candidate):
    assert candidate([]) == []

def test_check():
	check(f)