def f(num):
    """"""
    ### Canonical solution below ###
    num.append(num[-1])
    return num

def check(candidate):
    assert candidate([-70, 20, 9, 1]) == [-70, 20, 9, 1, 1]

def test_check():
	check(f)