def f(text, old, new):
    """"""
    ### Canonical solution below ###
    index = text.rfind(old, 0, text.find(old))
    result = list(text)
    while index > 0:
        result[index:index+len(old)] = new
        index = text.rfind(old, 0, index)
    return ''.join(result)

def check(candidate):
    assert candidate('jysrhfm ojwesf xgwwdyr dlrul ymba bpq', 'j', '1') == 'jysrhfm ojwesf xgwwdyr dlrul ymba bpq'

def test_check():
	check(f)