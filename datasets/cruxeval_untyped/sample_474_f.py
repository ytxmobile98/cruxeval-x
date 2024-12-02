def f(txt, marker):
    """"""
    ### Canonical solution below ###
    a = []
    lines = txt.split('\n')
    for line in lines:
        a.append(line.center(marker))
    return '\n'.join(a)

def check(candidate):
    assert candidate('#[)[]>[^e>\n 8', -5) == '#[)[]>[^e>\n 8'

def test_check():
	check(f)