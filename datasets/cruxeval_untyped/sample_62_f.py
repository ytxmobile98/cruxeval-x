def f(user):
    """"""
    ### Canonical solution below ###
    if len(list(user.keys())) > len(list(user.values())):
        return tuple(user.keys())
    return tuple(user.values())

def check(candidate):
    assert candidate({"eating" : "ja", "books" : "nee", "piano" : "coke", "excitement" : "zoo"}) == ('ja', 'nee', 'coke', 'zoo')

def test_check():
	check(f)