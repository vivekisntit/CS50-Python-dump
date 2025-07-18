import pytest
from asn7_3 import convert

def main():
    test_correct()
    test_wrong()

def test_correct():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00"
    assert convert("10 AM to 8:50 PM")=="10:00 to 20:50"

def test_wrong():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

if __name__ == "__main__":
    main()
