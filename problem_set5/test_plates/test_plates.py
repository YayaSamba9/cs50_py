from plates import is_valid

def test_isvalid_true():
    assert is_valid("CS") == True
    assert is_valid("CS50")== True


def test_isvalid_false():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("OVERSLEEP") == False
    assert is_valid("CS!") == False
    assert is_valid("12")== False
