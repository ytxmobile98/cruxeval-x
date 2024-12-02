def f(text, suffix):
    """"""
    ### Canonical solution below ###
    text += suffix
    while text[-len(suffix):] == suffix:
        text = text[:-1]
    return text

def check(candidate):
    assert candidate('faqo osax f', 'f') == 'faqo osax '

def test_check():
	check(f)