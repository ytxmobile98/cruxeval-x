def f(value, char):
    """"""
    ### Canonical solution below ###
    total = 0
    for c in value:
        if c == char or c == char.lower():
            total += 1
    return total

def check(candidate):
    assert candidate('234rtccde', 'e') == 1

def test_check():
	check(f)