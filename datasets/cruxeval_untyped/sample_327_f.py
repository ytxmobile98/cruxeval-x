def f(lst):
    """"""
    ### Canonical solution below ###
    new = list()
    i = len(lst)-1
    for _ in range(len(lst)):
        if i%2 == 0:
            new.append(-lst[i])
        else:
            new.append(lst[i])
        i -= 1
    return new

def check(candidate):
    assert candidate([1, 7, -1, -3]) == [-3, 1, 7, -1]

def test_check():
	check(f)