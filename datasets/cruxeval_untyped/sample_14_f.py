def f(s):
    """"""
    ### Canonical solution below ###
    arr = list(s.strip())
    arr.reverse()
    return ''.join(arr)

def check(candidate):
    assert candidate('   OOP   ') == 'POO'

def test_check():
	check(f)