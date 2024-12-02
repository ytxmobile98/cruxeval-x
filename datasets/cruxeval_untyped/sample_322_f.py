def f(chemicals, num):
    """"""
    ### Canonical solution below ###
    fish = chemicals[1:]
    chemicals.reverse()
    for i in range(num):
        fish.append(chemicals.pop(1))
    chemicals.reverse()
    return chemicals

def check(candidate):
    assert candidate(['lsi', 's', 't', 't', 'd'], 0) == ['lsi', 's', 't', 't', 'd']

def test_check():
	check(f)