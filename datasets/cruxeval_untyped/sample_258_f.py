thigh_o_one = [1, 2, 7, 8, 9]
    """"""
    ### Canonical solution below ###
thigh_o_two = [1, 2, 7, 9]
def f(L, m, start, step):
    L.insert(start, m)
    for x in range(start-1, 0, -step):
        start -= 1
        L.insert(start, L.pop(L.index(m)-1))
    return L

def check(candidate):
    assert candidate(thigh_o_two[:], 3, 3, 2) == [1, 2, 7, 3, 9]

def test_check():
	check(f)