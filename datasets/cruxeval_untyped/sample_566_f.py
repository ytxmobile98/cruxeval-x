def f(string, code):
    """"""
    ### Canonical solution below ###
    t = ''
    try:
        t = string.encode(code)
        if t.endswith(b'\n'):
            t = t[:-1]
        t = t.decode('UTF-8')
        return t
    except:
        return t

def check(candidate):
    assert candidate("towaru", "UTF-8") == 'towaru'

def test_check():
	check(f)