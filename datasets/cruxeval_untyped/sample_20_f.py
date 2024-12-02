def f(text):
    """"""
    ### Canonical solution below ###
    result = ''
    for i in range(len(text)-1, -1, -1):
        result += text[i]
    return result

def check(candidate):
    assert candidate('was,') == ',saw'

def test_check():
	check(f)