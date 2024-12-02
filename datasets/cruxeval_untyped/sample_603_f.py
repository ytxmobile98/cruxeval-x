def f(sentences):
    """"""
    ### Canonical solution below ###
    if all([sentence.isdecimal() for sentence in sentences.split('.')]):
        return 'oscillating' 
    else:
        return 'not oscillating'

def check(candidate):
    assert candidate('not numbers') == 'not oscillating'

def test_check():
	check(f)