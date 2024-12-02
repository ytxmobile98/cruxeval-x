def f(str,toget):
    """"""
    ### Canonical solution below ###
    if str.startswith(toget): return str[len(toget):]
    else: return str

def check(candidate):
    assert candidate('fnuiyh', 'ni') == 'fnuiyh'

def test_check():
	check(f)