def f(strand, zmnc):
    """"""
    ### Canonical solution below ###
    poz = strand.find(zmnc)
    while poz != -1:
        strand = strand[poz + 1:]
        poz = strand.find(zmnc)
    return strand.rfind(zmnc)

def check(candidate):
    assert candidate('', 'abc') == -1

def test_check():
	check(f)