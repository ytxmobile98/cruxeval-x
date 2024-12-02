def f(dictionary, key):
    """"""
    ### Canonical solution below ###
    del dictionary[key]
    if min(dictionary) == key:
        key = list(dictionary)[0]
    return key

def check(candidate):
    assert candidate({'Iron Man': 4, 'Captain America': 3, 'Black Panther': 0,'Thor': 1, 'Ant-Man': 6}, 'Iron Man') == 'Iron Man'

def test_check():
	check(f)