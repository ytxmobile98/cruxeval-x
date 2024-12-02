def f(letters):
    """"""
    ### Canonical solution below ###
    letters_only = letters.strip("., !?*")
    return "....".join(letters_only.split(" "))

def check(candidate):
    assert candidate("h,e,l,l,o,wo,r,ld,") == 'h,e,l,l,o,wo,r,ld'

def test_check():
	check(f)