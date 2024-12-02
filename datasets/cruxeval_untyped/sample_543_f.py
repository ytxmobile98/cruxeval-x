def f(item):
    """"""
    ### Canonical solution below ###
    modified = item.replace('. ', ' , ').replace('&#33; ', '! ').replace('. ', '? ').replace('. ', '. ')
    return modified[0].upper() + modified[1:]

def check(candidate):
    assert candidate('.,,,,,. منبت') == '.,,,,, , منبت'

def test_check():
	check(f)