def f(text):
    """"""
    ### Canonical solution below ###
    return max(text.find(ch) for ch in 'aeiou')

def check(candidate):
    assert candidate("qsqgijwmmhbchoj") == 13

def test_check():
	check(f)