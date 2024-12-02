def f(s, separator):
    """"""
    ### Canonical solution below ###
    for i in range(len(s)):
        if s[i] == separator:
            new_s = list(s)
            new_s[i] = '/'
            return ' '.join(new_s)

def check(candidate):
    assert candidate('h grateful k', ' ') == 'h / g r a t e f u l   k'

def test_check():
	check(f)