def f(perc, full):
    """"""
    ### Canonical solution below ###
    reply = ""
    i = 0
    while perc[i] == full[i] and i < len(full) and i < len(perc):
        if perc[i] == full[i]:
            reply += "yes "
        else:
            reply += "no "
        i += 1
    return reply

def check(candidate):
    assert candidate("xabxfiwoexahxaxbxs", "xbabcabccb") == 'yes '

def test_check():
	check(f)