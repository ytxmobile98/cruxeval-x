def f(text, pre):
    """"""
    ### Canonical solution below ###
    if not text.startswith(pre):
        return text
    return text.removeprefix(pre)

def check(candidate):
    assert candidate('@hihu@!', '@hihu') == '@!'

def test_check():
	check(f)