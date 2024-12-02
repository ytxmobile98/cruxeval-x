def f(file):
    """"""
    ### Canonical solution below ###
    return file.index('\n')

def check(candidate):
    assert candidate("n wez szize lnson tilebi it 504n.\n") == 33

def test_check():
	check(f)