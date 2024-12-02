def f(text, value):
    """"""
    ### Canonical solution below ###
    text_list = list(text)
    text_list.append(value)
    return ''.join(text_list)

def check(candidate):
    assert candidate('bcksrut', 'q') == 'bcksrutq'

def test_check():
	check(f)