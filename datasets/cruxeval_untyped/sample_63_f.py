def f(text, prefix):
    """"""
    ### Canonical solution below ###
    while text.startswith(prefix):
        text = text[len(prefix):] or text
    return text

def check(candidate):
    assert candidate('ndbtdabdahesyehu', 'n') == 'dbtdabdahesyehu'

def test_check():
	check(f)