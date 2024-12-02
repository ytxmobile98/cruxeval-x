def f(a, b):
    """"""
    ### Canonical solution below ###
    if a < b:
        return (b, a)
    return (a, b)

def check(candidate):
    assert candidate('ml', 'mv') == ('mv', 'ml')

def test_check():
	check(f)