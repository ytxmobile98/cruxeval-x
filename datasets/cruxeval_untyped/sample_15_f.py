def f(text, wrong, right):
    """"""
    ### Canonical solution below ###
    new_text = text.replace(wrong, right)
    return new_text.upper()

def check(candidate):
    assert candidate("zn kgd jw lnt", "h", "u") == 'ZN KGD JW LNT'

def test_check():
	check(f)