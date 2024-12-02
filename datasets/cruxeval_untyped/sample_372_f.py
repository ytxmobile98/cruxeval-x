def f(list_, num):
    """"""
    ### Canonical solution below ###
    temp = []
    for i in list_:
        i = num // 2 * ('%s,' % i)
        temp.append(i)
    return temp

def check(candidate):
    assert candidate(['v'], 1) == ['']

def test_check():
	check(f)