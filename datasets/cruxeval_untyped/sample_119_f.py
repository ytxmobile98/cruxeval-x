def f(text):
    """"""
    ### Canonical solution below ###
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].swapcase()
        else:
            result += text[i]
    return result

def check(candidate):
    assert candidate("vsnlygltaw") == 'VsNlYgLtAw'

def test_check():
	check(f)