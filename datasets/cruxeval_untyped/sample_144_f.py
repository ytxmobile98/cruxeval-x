def f(vectors):
    """"""
    ### Canonical solution below ###
    sorted_vecs = []
    for vec in vectors:
        vec.sort()
        sorted_vecs.append(vec)
    return sorted_vecs

def check(candidate):
    assert candidate([]) == []

def test_check():
	check(f)