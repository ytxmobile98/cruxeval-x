def f(text, digit):
    """"""
    ### Canonical solution below ###
    #different than previous? Just count instances digit
    count = text.count(digit)
    return int(digit) * count

def check(candidate):
    assert candidate('7Ljnw4Lj', '7') == 7

def test_check():
	check(f)