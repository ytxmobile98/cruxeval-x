def f(s):
    """"""
    ### Canonical solution below ###
    return s.upper()

def check(candidate):
    assert candidate("Jaafodsfa SOdofj AoaFjIs  JAFasIdfSa1") == 'JAAFODSFA SODOFJ AOAFJIS  JAFASIDFSA1'

def test_check():
	check(f)