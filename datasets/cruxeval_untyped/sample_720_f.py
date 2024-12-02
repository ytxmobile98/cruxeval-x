def f(items, item):
    """"""
    ### Canonical solution below ###
    while items[-1] == item:
        items.pop()
    items.append(item)
    return len(items)

def check(candidate):
    assert candidate('bfreratrrbdbzagbretaredtroefcoiqrrneaosf'.split('-'), 'n') == 2

def test_check():
	check(f)