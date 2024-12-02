def f(text, char):
    """"""
    ### Canonical solution below ###
    count = text.count(char*2)
    return text[count:]

def check(candidate):
    assert candidate('vzzv2sg', 'z') == 'zzv2sg'

def test_check():
	check(f)