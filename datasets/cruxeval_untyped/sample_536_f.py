def f(cat):
    """"""
    ### Canonical solution below ###
    digits = 0
    for char in cat:
        if char.isdigit():
            digits += 1
    return digits

def check(candidate):
    assert candidate('C24Bxxx982ab') == 5

def test_check():
	check(f)