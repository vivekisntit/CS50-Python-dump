from asn8_1 import word

def main():
    test_correct()

def test_correct():
    assert word(283680)=="two hundred eighty-three thousand, six hundred eighty"
    assert word(548640)=="five hundred forty-eight thousand, six hundred forty"

if __name__ == "__main__":
    main()
