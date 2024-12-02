def f(char_map, text):
    """"""
    ### Canonical solution below ###
    new_text = ''
    for ch in text:
        val = char_map.get(ch)
        if val is None:
            new_text += ch
        else:
            new_text += val
    return new_text

def check(candidate):
    assert candidate({}, 'hbd') == 'hbd'

def test_check():
	check(f)