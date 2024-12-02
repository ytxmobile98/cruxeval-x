def f(c, st, ed):
    """"""
    ### Canonical solution below ###
    d = {}
    a, b = 0, 0
    for x, y in c.items():
        d[y] = x
        if y == st:
            a = x
        if y == ed:
            b = x
    w = d[st]
    return (w, b) if a > b else (b, w)

def check(candidate):
    assert candidate({'TEXT': 7, 'CODE': 3}, 7, 3) == ('TEXT', 'CODE')

def test_check():
	check(f)