def f(a, b, c, d, e):
    """"""
    ### Canonical solution below ###
    key = d
    if key in a:
        num = a.pop(key)
    if b > 3:
        return ''.join(c)
    else:
        return num

def check(candidate):
    assert candidate({7: 'ii5p', 1: 'o3Jwus', 3: 'lot9L', 2: '04g', 9: 'Wjf', 8: '5b', 0: 'te6', 5: 'flLO', 6: 'jq', 4: 'vfa0tW'}, 4, 'Wy', 'Wy', 1.0) == 'Wy'

def test_check():
	check(f)