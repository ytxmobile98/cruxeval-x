def f(haystack, needle):
    """"""
    ### Canonical solution below ###
    for i in range(haystack.find(needle), -1, -1):
        if haystack[i:] == needle:
            return i
    return -1

def check(candidate):
    assert candidate("345gerghjehg", "345") == -1

def test_check():
	check(f)