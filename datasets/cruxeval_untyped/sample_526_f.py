def f(label1, char, label2, index):
    """"""
    ### Canonical solution below ###
    m = label1.rindex(char)
    if m >= index:
        return label2[:m - index + 1]
    return label1 + label2[index - m - 1:]

def check(candidate):
    assert candidate('ekwies', 's', 'rpg', 1) == 'rpg'

def test_check():
	check(f)