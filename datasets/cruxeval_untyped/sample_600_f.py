def f(array):
    """"""
    ### Canonical solution below ###
    just_ns = list(map(lambda num: 'n'*num, array))
    final_output = []
    for wipe in just_ns:
        final_output.append(wipe)
    return final_output

def check(candidate):
    assert candidate([]) == []

def test_check():
	check(f)