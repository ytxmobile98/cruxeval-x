def f(sentence):
    """"""
    ### Canonical solution below ###
    ls = list(sentence)
    for letter in ls:
        if not letter.istitle():
            ls.remove(letter)
    return ''.join(ls)

def check(candidate):
    assert candidate('XYZ LittleRedRidingHood LiTTleBIGGeXEiT fault') == 'XYZLtRRdnHodLTTBIGGeXET fult'

def test_check():
	check(f)