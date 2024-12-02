def f(val, text):
    """"""
    ### Canonical solution below ###
    indices = [index for index in range(len(text)) if text[index] == val]
    if len(indices) == 0:
        return -1
    else:
        return indices[0]

def check(candidate):
    assert candidate('o', 'fnmart') == -1

def test_check():
	check(f)