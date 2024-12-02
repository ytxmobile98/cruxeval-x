def f(str):
    """"""
    ### Canonical solution below ###
    if str.isalnum():
        return "True"
    return "False"

def check(candidate):
    assert candidate('777') == 'True'

def test_check():
	check(f)