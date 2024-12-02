def f(text, width):
    """"""
    ### Canonical solution below ###
    lines = [line.center(width) for line in text.split('\n')]
    return '\n'.join(lines)

def check(candidate):
    assert candidate("a\nbc\n\nd\nef", 5) == '  a  \n  bc \n     \n  d  \n  ef '

def test_check():
	check(f)