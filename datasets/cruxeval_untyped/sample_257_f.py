def f(text):
    """"""
    ### Canonical solution below ###
    ls = []
    for x in text:
        ls.append(x.splitlines())
    return ls

def check(candidate):
    assert candidate(['Hello World\n"I am String"']) == [['Hello World', '"I am String"']]

def test_check():
	check(f)