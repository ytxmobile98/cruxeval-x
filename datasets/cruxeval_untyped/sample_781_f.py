def f(s, ch):
    """"""
    ### Canonical solution below ###
    if ch not in s:
        return ''
    s = s.partition(ch)[2][::-1]
    for i in range(len(s)):
        s = s.partition(ch)[2][::-1]
    return s

def check(candidate):
    assert candidate('shivajimonto6', '6') == ''

def test_check():
	check(f)