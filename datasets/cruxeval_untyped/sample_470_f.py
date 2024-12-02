def f(number):
    """"""
    ### Canonical solution below ###
    transl = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    result = []
    for key, value in transl.items():
        if value % number == 0:
            result.append(key)
    return result

def check(candidate):
    assert candidate(2) == ['B', 'D']

def test_check():
	check(f)