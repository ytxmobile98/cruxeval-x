def f(names):
    """"""
    ### Canonical solution below ###
    if names == []:
        return ""
    smallest = names[0]
    for name in names[1:]:
        if name < smallest:
            smallest = name
    names.remove(smallest)
    return names.join(smallest)

def check(candidate):
    assert candidate([]) == ''

def test_check():
	check(f)