def f(text):
    """"""
    ### Canonical solution below ###
    for p in ['acs', 'asp', 'scn']:
        text = text.removeprefix(p) + ' '
    return text.removeprefix(' ')[:-1]

def check(candidate):
    assert candidate('ilfdoirwirmtoibsac') == 'ilfdoirwirmtoibsac  '

def test_check():
	check(f)