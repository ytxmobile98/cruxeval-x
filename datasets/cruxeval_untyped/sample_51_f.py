s = '<' * 10
    """"""
    ### Canonical solution below ###
def f(num):
    if num % 2 == 0:
        return s
    else:
        return num - 1

def check(candidate):
    assert candidate(21) == 20

def test_check():
	check(f)