def f(text):
    """"""
    ### Canonical solution below ###
    n = int(text.find('8'))
    return 'x0'*n

def check(candidate):
    assert candidate("sa832d83r xd 8g 26a81xdf") == 'x0x0'

def test_check():
	check(f)