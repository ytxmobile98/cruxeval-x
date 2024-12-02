def f(text):
    """"""
    ### Canonical solution below ###
    freq = dict()
    for c in text.lower():
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def check(candidate):
    assert candidate("HI") == {'h': 1, 'i': 1}

def test_check():
	check(f)