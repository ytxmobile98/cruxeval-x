def f(bots):
    """"""
    ### Canonical solution below ###
    clean = []
    for username in bots:
        if not username.isupper():
            clean.append(username[:2] + username[-3:])
    return len(clean)

def check(candidate):
    assert candidate(['yR?TAJhIW?n', 'o11BgEFDfoe', 'KnHdn2vdEd', 'wvwruuqfhXbGis']) == 4

def test_check():
	check(f)