def f(n):
    """"""
    ### Canonical solution below ###
    b = list(str(n))
    for i in range(2,len(b)): b[i] += '+'
    return b

def check(candidate):
    assert candidate(44) == ['4', '4']

def test_check():
	check(f)