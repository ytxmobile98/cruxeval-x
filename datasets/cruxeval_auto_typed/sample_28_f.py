from typing import List, Dict, Tuple

def f(mylist: List[int]) -> bool:
    """"""
    ### Canonical solution below ###
    revl = myList[:]
    revl.reverse()
    mylist.sort(reverse=True)
    return mylist == revl

### Unit tests below ###
def check(candidate):
    assert candidate([5, 8]) == True

def test_check():
    check(f)

