def f(s, c1, c2):
    """"""
    ### Canonical solution below ###
    if s == '':
        return s
    ls = s.split(c1)
    for index, item in enumerate(ls):
        if c1 in item:
            ls[index] = item.replace(c1, c2, 1)
    return c1.join(ls)

def check(candidate):
    assert candidate('', 'mi', 'siast') == ''

def test_check():
	check(f)