def f(mylist):
    """"""
    ### Canonical solution below ###
    revl = mylist[:]
    revl.reverse()
    mylist.sort(reverse=True)
    return mylist == revl

def check(candidate):
    assert candidate([5, 8]) == True

def test_check():
	check(f)