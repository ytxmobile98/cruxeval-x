def f(price, product):
    """"""
    ### Canonical solution below ###
    inventory = ['olives', 'key', 'orange']
    if product not in inventory:
        return price
    else:
        price *=.85
        inventory.remove(product)
    return price

def check(candidate):
    assert candidate(8.50, 'grapes') == 8.5

def test_check():
	check(f)