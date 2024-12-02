def f(concat, di):
    """"""
    ### Canonical solution below ###
    count = len(di)
    for i in range(count):
        if di[str(i)] in concat:
            di.pop(str(i))
    return "Done!"

def check(candidate):
    assert candidate('mid', {'0':'q','1':'f','2':'w','3':'i'}) == 'Done!'

def test_check():
	check(f)