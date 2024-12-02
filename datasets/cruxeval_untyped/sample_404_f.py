def f(no):
    """"""
    ### Canonical solution below ###
    d = dict.fromkeys(no, False) 
    return sum([1 for i in d.keys()])

def check(candidate):
    assert candidate(['l', 'f', 'h', 'g', 's', 'b']) == 6

def test_check():
	check(f)