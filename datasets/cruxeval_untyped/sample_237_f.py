def f(text, char):
    """"""
    ### Canonical solution below ###
    if char in text:
        suff, char, pref = text.partition(char)
        pref = suff[:-len(char)] + suff[len(char):] + char + pref
        return suff + char + pref
    return text

def check(candidate):
    assert candidate('uzlwaqiaj', 'u') == 'uuzlwaqiaj'

def test_check():
	check(f)