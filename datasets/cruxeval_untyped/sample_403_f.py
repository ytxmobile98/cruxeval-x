def f(full, part):
    """"""
    ### Canonical solution below ###
    length = len(part)
    index = full.find(part)
    count = 0
    while index >= 0:
        full = full[index + length:]
        index = full.find(part)
        count += 1
    return count

def check(candidate):
    assert candidate('hrsiajiajieihruejfhbrisvlmmy', 'hr') == 2

def test_check():
	check(f)