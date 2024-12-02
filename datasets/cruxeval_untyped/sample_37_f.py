def f(text):
    """"""
    ### Canonical solution below ###
    text_arr = []
    for j in range(len(text)):
        text_arr.append(text[j:])
    return text_arr

def check(candidate):
    assert candidate('123') == ['123', '23', '3']

def test_check():
	check(f)