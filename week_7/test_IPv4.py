from asn7_1_IPv4 import validate

def main():
    test_format()
    test_range()


def test_format():
    assert validate(r"1.2.3.4")==True
    assert validate(r"1.2.3")==False
    assert validate(r"1.2")==False
    assert validate(r"1")==False

def test_range():
    assert validate(r"255.255.255.255")==True
    assert validate(r"512.1.1.1")==False
    assert validate(r"1.512.1.1")==False
    assert validate(r"1.1.512.1")==False
    assert validate(r"1.1.1.512")==False



if __name__ == "__main__":
    main()

# from asn7_1_IPv4 import validate

# def test_correct():
#     assert validate("127.0.0.1")=="True"
# def test_wrong():
#     assert validate("512.512.512.512")=="False"
# def test_wrong2():
#     assert validate("192.168.001.1")=="False"
# def test_kitty():
#     assert validate("cat")=="False"