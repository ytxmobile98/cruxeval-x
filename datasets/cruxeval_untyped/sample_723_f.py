def f(text, separator):
    """"""
    ### Canonical solution below ###
    splitted = text.splitlines()
    if separator:
        return [' '.join(s) for s in splitted]
    else:
        return splitted

def check(candidate):
    assert candidate('dga nqdk\rull qcha kl', 1) == ['d g a   n q d k', 'u l l   q c h a   k l']

def test_check():
	check(f)