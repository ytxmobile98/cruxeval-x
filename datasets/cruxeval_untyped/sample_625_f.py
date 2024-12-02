def f(text):
    """"""
    ### Canonical solution below ###
    count = 0
    for i in text:
        if i in '.?!.,':
            count += 1
    return count

def check(candidate):
    assert candidate("bwiajegrwjd??djoda,?") == 4

def test_check():
	check(f)