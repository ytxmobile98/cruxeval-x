def f(lines):
    """"""
    ### Canonical solution below ###
    for i in range(len(lines)):
        lines[i] = lines[i].center(len(lines[-1]))
    return lines

def check(candidate):
    assert candidate(['dZwbSR', 'wijHeq', 'qluVok', 'dxjxbF']) == ['dZwbSR', 'wijHeq', 'qluVok', 'dxjxbF']

def test_check():
	check(f)