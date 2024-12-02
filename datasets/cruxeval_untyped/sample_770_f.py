def f(line, char):
    """"""
    ### Canonical solution below ###
    count = line.count(char)
    for i in range(count+1, 0, -1):
        line = line.center(len(line)+i // len(char), char)
    return line

def check(candidate):
    assert candidate('$78'.upper(), '$') == '$$78$$'

def test_check():
	check(f)