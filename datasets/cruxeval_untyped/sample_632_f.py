def f(list):
    """"""
    ### Canonical solution below ###
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                list.sort()
    return list

def check(candidate):
    assert candidate([63, 0, 1, 5, 9, 87, 0, 7, 25, 4]) == [0, 0, 1, 4, 5, 7, 9, 25, 63, 87]

def test_check():
	check(f)