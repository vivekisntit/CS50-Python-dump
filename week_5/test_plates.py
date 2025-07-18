from plates import is_valid

# def test_two_letters():
#     assert is_valid("ss24")==True
# def test_max():
#     assert is_valid("fgu39932")==False
# def test_min():
#     assert is_valid("0jk")==False
# def test_min_letters():
#     assert is_valid("ww")==True
# def test_mid_nums():
#     assert is_valid("ww7ger")==False
# def test_puncs():
#     assert is_valid("ww3,5")==False

def test_two_letters():
    assert is_valid("12")==False
def test_max():
    assert is_valid("CS50P")==False
def test_min():
    assert is_valid("PI3.14")==False
def test_min_letters():
    assert is_valid("H")==False
def test_mid_nums():
    assert is_valid("OUTATIME")==False
def test_puncs():
    assert is_valid("CS05")==False