def f(marks):
    """"""
    ### Canonical solution below ###
    highest = 0
    lowest = 100
    for value in marks.values():
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value
    return highest, lowest

def check(candidate):
    assert candidate({'x': 67, 'v': 89, '': 4, 'alij': 11, 'kgfsd': 72, 'yafby': 83}) == (89, 4)

def test_check():
	check(f)