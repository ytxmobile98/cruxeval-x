def f(string, substring):
    """"""
    ### Canonical solution below ###
    while string.startswith(substring):
        string = string[len(substring):len(string)]
    return string

def check(candidate):
    assert candidate('', 'A') == ''

def test_check():
	check(f)