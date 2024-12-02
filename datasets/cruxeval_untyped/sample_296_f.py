def f(url):
    """"""
    ### Canonical solution below ###
    return url.removeprefix('http://www.')

def check(candidate):
    assert candidate("https://www.www.ekapusta.com/image/url") == 'https://www.www.ekapusta.com/image/url'

def test_check():
	check(f)