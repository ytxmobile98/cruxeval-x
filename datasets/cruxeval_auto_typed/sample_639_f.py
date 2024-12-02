from typing import List, Dict, Tuple

def f(perc: str, full: str) -> str:
    """"""
    ### Canonical solution below ###
    reply = ''
    i = 0
    while perc[i] == full[i] and i < len(full) and (i < len(perc)):
        if perc[i] == full[i]:
            reply += 'yes '
        else:
            reply += 'no '
        i += 1
    return reply

### Unit tests below ###
def check(candidate):
    assert candidate('xabxfiwoexahxaxbxs', 'xbabcabccb') == 'yes '

def test_check():
    check(f)

