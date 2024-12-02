def f(title):
    """"""
    ### Canonical solution below ###
    return title.lower()

def check(candidate):
    assert candidate('   Rock   Paper   SCISSORS  ') == '   rock   paper   scissors  '

def test_check():
	check(f)