def f(items, target):
    """"""
    ### Canonical solution below ###
    for i in items.split():
        if i in target:
            return items.index(i)+1
        if i.index('.') == len(i)-1 or i.index('.') == 0:
            return 'error'
    return '.'

def check(candidate):
    assert candidate("qy. dg. rnvprt rse.. irtwv tx..", "wtwdoacb") == 'error'

def test_check():
	check(f)