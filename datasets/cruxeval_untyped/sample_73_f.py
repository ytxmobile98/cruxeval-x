def f(row):
    """"""
    ### Canonical solution below ###
    return (row.count('1'), row.count('0'))

def check(candidate):
    assert candidate("100010010") == (3, 6)

def test_check():
	check(f)