def f(st, pattern):
    """"""
    ### Canonical solution below ###
    for p in pattern:
        if not st.startswith(p): return False
        st = st[len(p):]
    return True

def check(candidate):
    assert candidate('qwbnjrxs', ['jr', 'b', 'r', 'qw']) == False

def test_check():
	check(f)