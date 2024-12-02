def f(text):
    """"""
    ### Canonical solution below ###
    topic, sep, problem = text.rpartition('|')
    if problem == 'r':
        problem = topic.replace('u', 'p')
    return topic, problem

def check(candidate):
    assert candidate('|xduaisf') == ('', 'xduaisf')

def test_check():
	check(f)