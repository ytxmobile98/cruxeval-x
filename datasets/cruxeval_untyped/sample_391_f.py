def f(students):
    """"""
    ### Canonical solution below ###
    seatlist = students
    seatlist.reverse()
    cnt = 0
    for cnt in range(len(seatlist)):
        cnt += 2
        seatlist[cnt - 1:cnt] = ['+']
    seatlist.append('+')
    return seatlist

def check(candidate):
    assert candidate(['r', '9']) == ['9', '+', '+', '+']

def test_check():
	check(f)