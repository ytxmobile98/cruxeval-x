def f(text, characters):
    """"""
    ### Canonical solution below ###
    character_list = list(characters) + [' ', '_']

    i = 0
    while i < len(text) and text[i] in character_list:
        i += 1

    return text[i:]

def check(candidate):
    assert candidate("2nm_28in", "nm") == '2nm_28in'

def test_check():
	check(f)