def f(text):
    """"""
    ### Canonical solution below ###
    return text[-1] + text[:-1]

def check(candidate):
    assert candidate('hellomyfriendear') == 'rhellomyfriendea'

def test_check():
	check(f)