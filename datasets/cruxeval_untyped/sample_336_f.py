def f(s, sep):
    """"""
    ### Canonical solution below ###
    s += sep
    return s.rpartition(sep)[0]

def check(candidate):
    assert candidate('234dsfssdfs333324314', 's') == '234dsfssdfs333324314'

def test_check():
	check(f)