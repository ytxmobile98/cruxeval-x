def f(d, get_ary):
    """"""
    ### Canonical solution below ###
    result = []
    for key in get_ary:
        result.append(d.get(key))
    return result

def check(candidate):
    assert candidate({3: "swims like a bull"}, [3, 2, 'c', True, 5]) == ['swims like a bull', None, None, None, None]

def test_check():
	check(f)