def f(sentence):
    """"""
    ### Canonical solution below ###
    if sentence == '':
        return ''
    sentence = sentence.replace('(', '')
    sentence = sentence.replace(')', '')
    return sentence.capitalize().replace(' ', '')

def check(candidate):
    assert candidate('(A (b B))') == 'Abb'

def test_check():
	check(f)