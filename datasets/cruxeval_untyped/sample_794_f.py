def f(line):
    """"""
    ### Canonical solution below ###
    a = []
    for c in line:
        if c.isalnum():
            a.append(c)
    return ''.join(a)

def check(candidate):
    assert candidate("\"\\%$ normal chars $%~ qwet42'") == 'normalcharsqwet42'

def test_check():
	check(f)