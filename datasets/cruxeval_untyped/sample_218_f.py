def f(string, sep):
    """"""
    ### Canonical solution below ###
    cnt = string.count(sep)
    return((string+sep) * cnt)[::-1]

def check(candidate):
    assert candidate('caabcfcabfc', 'ab') == 'bacfbacfcbaacbacfbacfcbaac'

def test_check():
	check(f)