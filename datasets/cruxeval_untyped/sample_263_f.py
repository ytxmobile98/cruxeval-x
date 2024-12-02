def f(base, delta):
    """"""
    ### Canonical solution below ###
    for j in range(len(delta)):
        for i in range(len(base)):
            if base[i] == delta[j][0]:
                assert delta[j][1] != base[i]
                base[i] = delta[j][1]
    return base

def check(candidate):
    assert candidate(["gloss", "banana", "barn", "lawn"], []) == ['gloss', 'banana', 'barn', 'lawn']

def test_check():
	check(f)