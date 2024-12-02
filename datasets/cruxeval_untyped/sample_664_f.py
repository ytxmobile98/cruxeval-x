def f(tags):
    """"""
    ### Canonical solution below ###
    resp = ""
    for key in tags:
        resp += key + " "
    return resp

def check(candidate):
    assert candidate({"3":"3","4":"5"}) == '3 4 '

def test_check():
	check(f)