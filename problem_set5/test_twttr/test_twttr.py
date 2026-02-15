from twttr import shorten

def test_shorten_lower():
    assert shorten ('hi') == 'h'
    assert shorten("hello")=="hll"
    assert shorten("aeuio") == ""

def test_shorten_capitalize():
    assert shorten("GOLMY")=="GLMY"
    assert shorten("AEUIO") == ""
    assert shorten("TAILLE") == "TLL"

def test_shorten_num():
    assert shorten("CS50") == "CS50"
    assert shorten("Yahya10") == "Yhy10"
    assert shorten("Numero21") == "Nmr21"

def test_shorten_ponctu() :
    assert shorten("Hi!")== "H!"
    assert shorten("What?") == "Wht?"
    assert shorten (".,") == ".,"