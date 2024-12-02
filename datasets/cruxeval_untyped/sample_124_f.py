def f(txt, sep, sep_count):
    """"""
    ### Canonical solution below ###
    o = ''
    while sep_count > 0 and txt.count(sep) > 0:
        o += txt.rsplit(sep, 1)[0] + sep
        txt = txt.rsplit(sep, 1)[1]
        sep_count -= 1
    return o + txt

def check(candidate):
    assert candidate('i like you', ' ', -1) == 'i like you'

def test_check():
	check(f)