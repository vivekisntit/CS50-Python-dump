import pytest
from fuel import convert, gauge

def main():
    test_correct()
    test_wrong()

def test_correct():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(71)=="71%"

def test_wrong():
    assert convert("3/5")==60
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("x/10")
    with pytest.raises(ValueError):
        convert("-7/10")
    with pytest.raises(ValueError):
        convert("4/1")
    with pytest.raises(ZeroDivisionError):
        convert("9/0")

if __name__ == "__main__":
    main()
