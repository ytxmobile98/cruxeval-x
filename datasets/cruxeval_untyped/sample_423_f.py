def f(selfie):
    """"""
    ### Canonical solution below ###
    lo = len(selfie)
    for i in range(lo-1, -1, -1):
        if selfie[i] == selfie[0]:
            selfie.remove(selfie[lo-1])
    return selfie

def check(candidate):
    assert candidate([4, 2, 5, 1, 3, 2, 6]) == [4, 2, 5, 1, 3, 2]

def test_check():
	check(f)