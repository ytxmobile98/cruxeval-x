def f(data):
    """"""
    ### Canonical solution below ###
    members = []
    for item in data:
        for member in data[item]:
            if member not in members:
                members.append(member)
    return sorted(members)

def check(candidate):
    assert candidate({'inf': ['a', 'b'], 'a': ["inf", "c"], 'd': ["inf"]}) == ['a', 'b', 'c', 'inf']

def test_check():
	check(f)