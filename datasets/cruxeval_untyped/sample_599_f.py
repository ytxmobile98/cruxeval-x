def f(a, b):
    """"""
    ### Canonical solution below ###
    a = b.join(a)
    lst = []
    for i in range(1, len(a)+1, 2):
        lst.append(a[i-1:][:i])
        lst.append(a[i-1:][i:])
    return lst

def check(candidate):
    assert candidate(["a", "b", "c"], " ") == ['a', ' b c', 'b c', '', 'c', '']

def test_check():
	check(f)