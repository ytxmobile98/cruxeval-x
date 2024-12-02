def f(numbers, prefix):
    """"""
    ### Canonical solution below ###
    return sorted(n[len(prefix):] if (len(n) > len(prefix) and n.startswith(prefix)) else n
                  for n in numbers)

def check(candidate):
    assert candidate(['ix', 'dxh', 'snegi', 'wiubvu'], '') == ['dxh', 'ix', 'snegi', 'wiubvu']

def test_check():
	check(f)