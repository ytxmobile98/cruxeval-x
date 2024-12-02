def f(text, chunks):
    """"""
    ### Canonical solution below ###
    return text.splitlines(chunks)

def check(candidate):
    assert candidate('/alcm@ an)t//eprw)/e!/d\nujv', 0) == ['/alcm@ an)t//eprw)/e!/d', 'ujv']

def test_check():
	check(f)