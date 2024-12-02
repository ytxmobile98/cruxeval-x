def f(input_string):
    """"""
    ### Canonical solution below ###
    table = str.maketrans('aioe', 'ioua')
    while 'a' in input_string or 'A' in input_string:
        input_string = input_string.translate(table)
    return input_string

def check(candidate):
    assert candidate('biec') == 'biec'

def test_check():
	check(f)